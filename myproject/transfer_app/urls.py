from django.conf.urls import url

from . import views







urlpatterns = [
    url(r'^$', views.login_view, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^home/transactions$', views.transactions, name='transactions'),
    url(r'^home/operations$', views.operations, name='operations'),
    url(r'^home/reporting$', views.reporting, name='reporting'),  
    url(r'^delete/$', views.delete, name='delete'),
    ]
    