from django.conf.urls import patterns, include, url
from sorokin_test2.accounts.views import ProfileView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
     url(r'^$', ProfileView.as_view(), name='home'),
)
