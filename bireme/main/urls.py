from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    
    (r'^$', 'main.views.dashboard'),
)