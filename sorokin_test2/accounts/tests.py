"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from sorokin_test2.accounts.models import Profile


class ProfileViewTestCase(WebTest):

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