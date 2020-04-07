import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import time
import json



#
# def weixin_page(request):
#     return render(request, 'weixin_index.html')
#
#
# def weixinbind(request):
#     """
#     appid 去公众号平台 - > 开发 -> 基本配置 里找。
#
#     redirect_uri 是成功以后的回调地址，是你自己的一个 url，要通过 urlEncode 进行编码
#
#     response_type 写 code
#
#     scope 可选填 snsapi_base 或 snsapi_userinfo
#
#     state 非必填，所以直接不加这个参数了
#
#     关于 python 的 urlEncode 可以使用：
#
#     import urllib.parse
#     s='https://xxx.com/api/weixin_bind_callback/'
#     urllib.parse.quote(s, safe='')
#
#     """
#     return HttpResponseRedirect('https://open.weixin.qq.com/connect/oauth2/authorize?appid=XXXXX&redirect_uri=https'
#                                 '%3A%2F%2FXXXXX.com%2Fweixin%2Fbind%2Fcallback%2F&response_type=code&scope'
#                                 '=snsapi_userinfo#wechat_redirect')
#
#
# def weixinbind_callback(request):
#     """
#     APPID 和 secret 去公众号平台 - > 开发 -> 基本配置 里找。
#
#     code 是返回的 code
#
#     grant_type 就写 authorization_code
#     """
#     code = request.GET.get('code')
#     state = request.GET.get('state')
#     print(code, state)
#     APPID = 'xxxxx'
#     secret = 'xxxxx'
#     r = requests.get(
#         'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' % (
#         APPID, secret, code)
#     )
#     # print(r.text)
#     d = json.loads(r.text)
#     # {
#     #   "access_token":"ACCESS_TOKEN",
#     #   "expires_in":7200,
#     #   "refresh_token":"REFRESH_TOKEN",
#     #   "openid":"OPENID",
#     #   "scope":"SCOPE"
#     # }
#     r = requests.get(
#         'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' % (d['access_token'], d['openid'])
#     )
#     # print(r.content)
#     dd = json.loads(r.content.decode('utf8'))
#     # {
#     #   "openid":" OPENID",
#     #   "nickname": NICKNAME,
#     #   "sex":"1",
#     #   "province":"PROVINCE",
#     #   "city":"CITY",
#     #   "country":"COUNTRY",
#     #   "headimgurl":       "http://thirdwx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46",
#     #   "privilege":[ "PRIVILEGE1" "PRIVILEGE2"     ],
#     #   "unionid": "o6_bmasdasdsad6_2sgVt7hMZOPfL"
#     # }
#     request.user.userprofile.openid = dd['openid']
#     request.user.userprofile.nickname = dd['nickname']
#     request.user.userprofile.wsex = dd['sex']
#     request.user.userprofile.province = dd['province']
#     request.user.userprofile.city = dd['city']
#     request.user.userprofile.country = dd['country']
#     request.user.userprofile.headimgurl = dd['headimgurl']
#     request.user.userprofile.privilege = json.dumps(dd['privilege'])
#     # request.user.userprofile.unionid = dd['unionid']
#     request.user.userprofile.refresh_token_time = time.time()
#     request.user.userprofile.save()
#     return HttpResponseRedirect('/weixin/')
