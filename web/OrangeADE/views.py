from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from importlib import import_module
SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
import datetime

def index(request):
    now = datetime.datetime.now()
    t = get_template('main_index.html')
    try:
        sid = request.session['sid']
    except:
        request.session.create()
        request.session['sid']=request.session.session_key
    html = t.render(Context({'current_date': now, 'session_id': request.session['sid'],
                             'user_agent': request.META['HTTP_USER_AGENT'], 'user_addr': request.META['REMOTE_ADDR']}))
    return HttpResponse(html)