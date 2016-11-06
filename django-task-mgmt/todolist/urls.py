from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tasks.api import TaskResource, UserResource
from tastypie.api import Api
from tasks.views import *

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(TaskResource())


urlpatterns = patterns('',
   url(r'^$', 'tasks.views.task_list'),
   url(r'^tasks/', include('tasks.urls')),
   # Session management
   url(r'^login/$', 'django.contrib.auth.views.login'),
   url(r'^logout/$', logout_page),
   url(r'^register/$', register_page),
   url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.html")),

   # Account management
   url(r'^api/', include(v1_api.urls)),
   url(r'^media/(?P<path>.*)$', "django.views.static.serve")
)
