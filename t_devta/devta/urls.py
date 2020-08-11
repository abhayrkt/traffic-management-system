"""t_devta URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('d_diversion',views.d_diversion,name='d_diversion'),
    path('view_news',views.view_news,name='view_news'),
    path('diversion_delete/<d_id>',views.diversion_delete,name='diversion_delete'),
    path('admin/', admin.site.urls),
    path('login',views.login,name='login'),
    path('login_1',views.login_1,name='login_1'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('contact',views.contact,name='contact'),
    path('error',views.error,name='error'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name = 'gallery'),
    path('news1',views.news1,name='news1'),
    path('article',views.article,name='article'),
    path('add_news',views.add_news,name='add_news'),
    path('article_details',views.article_details,name='article_details'),
    path('contact_form',views.contact_form,name='contact_form'),
    path('new_user',views.new_user,name='new_user'),
    path('p_login',views.p_login,name='p_login'),
    path('report',views.report,name='report'),
    path('report_1',views.report_1,name='report_1'),
    path('add_diverison',views.add_diversion,name='add_diversion'),
    path('view_diversion',views.view_diversion,name='view_diversion'),
    path('a_challan',views.a_challan,name='a_challan'),
    path('view_challan/<licence_no>',views.view_challan,name='view_challan'),
    path('i_challan',views.i_challan,name='i_challan'),
    path('view_user',views.view_user,name='view_user'),
    path('diversion_page',views.diversion_page,name='diversion_page'),
]
