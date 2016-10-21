from django.conf.urls import patterns, url
from .views import users_json, user_json

urlpatterns = patterns('',
                       url(r'^get_users/$', users_json),
                       url(r'^get_user/(\d+)/$', user_json),
                       )
