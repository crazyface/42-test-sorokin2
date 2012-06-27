from django.conf.urls import patterns, include, url
from sorokin_test2.accounts.views import ProfileEditView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
     url(r'^$', ProfileEditView.as_view(), name='home'),
     url(r'^accounts/login/$', 'django.contrib.auth.views.login',
         {'template_name': 'accounts/login.html'}, name='login'),
   url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name='logout')
)
