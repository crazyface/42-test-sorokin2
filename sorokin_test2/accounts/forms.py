from django import forms
from sorokin_test2.accounts.models import Profile
from django.contrib.admin.widgets import AdminDateWidget
from sorokin_test2.accounts.widgets import Calendar


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=Calendar)
    
    class Meta:
        model = Profile
        exclude = ['photo']