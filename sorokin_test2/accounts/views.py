# Create your views here.
from django.views.generic.detail import DetailView
from sorokin_test2.accounts.models import Profile


class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'

    def get_object(self, **kwargs):
        return self.model.objects.all()[0]