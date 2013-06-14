from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from models import *
from django import forms
from main.models import *

class ChangeUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', )

class ChangeProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ( 'degree', 'country', 'gender')