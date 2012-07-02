# Create your views here.
from django.views.generic.detail import DetailView
from sorokin_test2.accounts.models import Profile
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from sorokin_test2.accounts.forms import ProfileForm


class ProfileEditView(UpdateView):
    model = Profile
    success_url = reverse_lazy('home')
    form_class=ProfileForm

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=1)

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated():
            self.template_name = 'accounts/profile_detail.html'
        return super(ProfileEditView, self).get_context_data(**kwargs)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super(ProfileEditView, self).post(request, *args, **kwargs)

