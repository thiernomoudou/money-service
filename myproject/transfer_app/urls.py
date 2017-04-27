from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin


from . import views







urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', auth_views.login, {'template_name': 'login.html'},
        name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^home/transactions/$', views.transactions, name='transactions'),
    url(r'^home/operations/$', views.operations, name='operations'),
    url(r'^home/reporting/$', views.reporting, name='reporting'),  
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^home/reporting/summary/$', views.summary, name='summary'),
    ]
    