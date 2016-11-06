from django.conf.urls import patterns, url

from tasks import views


urlpatterns = patterns('',
                       url(r'^$', views.task_list, name='task_list'),
                       url(r'^new$', views.task_create, name='task_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.task_update, name='task_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.task_delete, name='task_delete'),
                       )