from django.conf.urls import patterns, include, url
from sorokin_test2.accounts.views import ProfileEditView, ProfileDetailView,\
    ajax_upload
from django.contrib.auth.decorators import login_required
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
     url(r'^$', ProfileDetailView.as_view(), name='home'),
     url(r'^edit/$', login_required(ProfileEditView.as_view()), name='edit'),
     url(r'^accounts/login/$', 'django.contrib.auth.views.login',
         {'template_name': 'accounts/login.html'}, name='login'),
     url(r'^accounts/upload/$', ajax_upload, name='upload'),
   url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name='logout')
)
