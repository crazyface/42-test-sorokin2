# Create your views here.
from django.views.generic.detail import DetailView
from sorokin_test2.accounts.models import Profile
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from sorokin_test2.accounts.forms import ProfileForm


class GetObjectMixIn(object):
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=1)


class ProfileDetailView(GetObjectMixIn,DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['form'] = ProfileForm()
        return context


class ProfileEditView(GetObjectMixIn, UpdateView):
    model = Profile
    success_url = reverse_lazy('home')
    form_class=ProfileForm

    def post(self, request, *args, **kwargs):
        return super(ProfileEditView, self).post(request, *args, **kwargs)

