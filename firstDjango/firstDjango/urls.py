"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# encoding=utf-8
from django.contrib import admin
from django.urls import path
from django_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.eval_index),
    path('add_eval/', views.add_eval),
    path('delete_eval/', views.delete_eval),
    path('latest_eval/', views.eval_list_time_order),
    path('classify/', views.get_eval_types),
    path('classify_list/', views.get_eval_type_detail),
    path('classify_list_time/', views.get_eval_type_detail_time),
    path('user_eval_list/', views.get_user_eval_list),
    path('user_review_list/', views.get_user_review_list),
    path('get_avatar/', views.get_avatar),
    # path('eval/<int:question_id>/', views.detail, name='detail'),
    # path('eval/<int:question_id>/results/', views.results, name='results'),
    # path('eval/<int:question_id>/vote/', views.vote, name='vote'),
]
