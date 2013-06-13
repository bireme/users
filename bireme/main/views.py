#! coding: utf-8
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import forms as auth_forms
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core import mail
from django.contrib.auth.models import User
from django.template import RequestContext
from utils.views import ACTIONS
from django.conf import settings
from datetime import datetime
from models import *
from forms import *
import mimetypes
import os

@login_required
def dashboard(request):
    
    user = request.user
    output = {}

    return render_to_response('main/index.html', output, context_instance=RequestContext(request))

