from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tasks.models import Task


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        fields = ['username', 'first_name', 'last_name', 'last_login']
        # authorization = Authorization()
        authentication = BasicAuthentication()


class TaskResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authentication = BasicAuthentication()
        authorization = Authorization()

    def get_object_list(self, request):
        return super(TaskResource, self).get_object_list(request).filter(user_id=request.user)
