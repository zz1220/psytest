"""认证中间件"""
import logging
import requests

from django.http.response import (
    HttpResponseForbidden,
    JsonResponse
)
from django.middleware.common import MiddlewareMixin

logger = logging.getLogger(__name__)


class AuthenticationMiddleware(MiddlewareMixin):
    """认证"""

    def __call__(self, request):
        """
        每个请求在到达中间级之前被执行
        """

        if request.path.startswith('/xadmin'):
            return self.get_response(request)

        ticket = request.META.get('HTTP_TICKET')
        if not ticket:
            return JsonResponse(data={'msg': '无效ticket，禁止访问该接口'}, status=400)
        headers = {
            'Ticket': ticket
        }
        url = 'http://132.232.91.198:9000/api/api-auth/'
        try:
            r = requests.get(url, headers=headers)
            if 200 == r.status_code:
                request.user_info = r.json().get('data', None)
                return self.get_response(request)
            return JsonResponse(
                data={
                    'msg': '无效Ticket',
                    'data': r.json()
                },
                status=r.status_code
            )
        except Exception as e:
            logger.error(f'request /api/api-auth/ failed: {e}')
            return JsonResponse(
                data={
                    'msg': '校验Ticket失败',
                    'data': e
                },
                status=500
            )
