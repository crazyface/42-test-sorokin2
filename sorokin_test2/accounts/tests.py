"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from sorokin_test2.accounts.models import Profile
from webtest.app import AppError


class ProfileDetailViewTestCase(WebTest):

    def test_view(self):
        response = self.app.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        expected = Profile.objects.get(pk=1)
        response = self.app.get(reverse('home'))
        self.assertEqual(expected, response.context['profile'])

    def test_template(self):
        expected = Profile.objects.get(pk=1)
        response = self.app.get(reverse('home'))
        self.assertContains(response, expected.first_name)
        self.assertContains(response, expected.email)

class ProfileEditlViewTestCase(WebTest):

    def test_edit_logout(self):
        self.assertRaises(AppError, self.app.post, reverse('edit'))

    def test_edit_login(self):
        auth_form = self.app.get(reverse('login')).form
        auth_form['username'] = 'admin'
        auth_form['password'] = 'admin'
        auth_form.submit()
        first_name = 'first_name test'
        last_name = 'last_name test'
        edit_form = self.app.get(reverse('edit')).form
        edit_form['first_name'] = first_name
        edit_form['last_name'] = last_name
        edit_form.submit()
        profile = Profile.objects.filter(id=1, first_name=first_name,
                                                        last_name=last_name)
        self.assertTrue(profile.exists())
    
    def test_edit_ajax(self):
        auth_form = self.app.get(reverse('login')).form
        auth_form['username'] = 'admin'
        auth_form['password'] = 'admin'
        auth_form.submit()
        first_name = 'first_name test2'
        last_name = 'last_name test2'
        edit_form = self.app.get(reverse('edit')).form
        edit_form['first_name'] = first_name
        edit_form['last_name'] = last_name
        response = self.app.post(reverse('edit'),
                                dict(edit_form.submit_fields()),
                        headers={'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        profile = Profile.objects.filter(id=1, first_name=first_name,
                                                        last_name=last_name)
        self.assertTrue(profile.exists())