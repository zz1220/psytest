"""PysTest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

import users
import xadmin
from django.urls import path
from psytests import views
from users import  views as user_view
from django.views.generic import RedirectView


def weixin_verify(request):
    return HttpResponse('PJRLUusp1NXyuD70')


urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    path('', views.eval_index),
    path('add_eval/', views.add_eval),
    path('delete_eval/', views.delete_eval),
    path('latest_eval/', views.eval_list_time_order),
    path('classify/', views.get_eval_types),
    path('classify_list/', views.get_eval_type_detail),
    path('classify_list_time/', views.get_eval_type_detail_time),
    path('user_eval_list/', views.get_user_eval_list),

    # path('weixin/', user_view.weixin_page),
    # path('weixin/bind/', user_view.weixinbind),
    # path('weixin/bind/callback/', user_view.weixinbind_callback),
    # path('MP_verify_PJRLUusp1NXyuD70.txt', weixin_verify),
]
