from django.conf.urls import patterns, include, url
from sorokin_test2.core.views import RequestView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
     url(r'^requests/(?P<order>reverse(?:/))?$', RequestView.as_view(), name='requests'),
)
