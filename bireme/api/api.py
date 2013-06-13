from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource

from main.models import *

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['first_name', 'last_name', 'email']
        allowed_methods = ['get', 'post']
        resource_name = 'user'

    def prepend_urls(self):
        return [
            url(r"^login%s$" % trailing_slash(), self.wrap_view('login'), name="api_login"),
            url(r'^logout%s$' % trailing_slash(), self.wrap_view('logout'), name='api_logout'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')
        service = data.get('service', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:

                # if not have roles in this service, is unauthorized
                if not roles:
                    return self.create_response(request, {'success': False, 'reason': "user doesn't allow to connect"}, HttpUnauthorized)
                
                output = {
                    'success': True,
                    'data': {
                        'user': user,
                    }
                }

                login(request, user)
                return self.create_response(request, output)
            else:
                return self.create_response(request, {'success': False, 'reason': 'disabled'}, HttpForbidden)
        else:
            return self.create_response(request, {'success': False, 'reason': 'incorrect'}, HttpUnauthorized)

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)