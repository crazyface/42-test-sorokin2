"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from sorokin_test2.accounts.models import Profile
from sorokin_test2.core.models import Request
from django.conf import settings
from sorokin_test2.core.middlewares import RequestStatistic
from sorokin_test2.core.contextprocessors import settings_processor
from django.test.client import RequestFactory
from mock import Mock


class RequestMiddlewareTestCase(WebTest):

    middleware = RequestStatistic()

    def test_right_request(self):
        path = reverse('home')
        self.app.get(path)
        self.assertTrue(Request.objects.filter(path=path).exists())

    def test_media_url(self):
        self.assertFalse(self.middleware.path_is_valid(settings.MEDIA_URL))

    def test_static_url(self):
        self.assertFalse(self.middleware.path_is_valid(settings.STATIC_URL))

    def test_favicon_url(self):
        self.assertFalse(self.middleware.path_is_valid('/favicon.ico'))


class RequestViewTestCase(WebTest):

    def test_view(self):
        response = self.app.get(reverse('core:requests'))
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        expected = [Request.objects.create(path='test1',
                               method='test1',
                               status_code='200',
                               params='{}')]
        response = self.app.get(reverse('core:requests'))
        self.assertEqual(expected, list(response.context['object_list']))

    def test_template(self):
        expected = [Request.objects.create(path='test1',
                                           method='test1',
                                           status_code='200',
                                           params='{}',),
                    Request.objects.create(path='test2',
                                           method='test2',
                                           status_code='200',
                                           params='{}',)
                    ]
        response = self.app.get(reverse('core:requests'))
        self.assertContains(response, expected[0].path)
        self.assertContains(response, expected[1].path)


class SettingsContextProcessorTestCase(WebTest):
    def test_settings_processor(self):

        self.assertTrue(settings_processor(Mock()).has_key('settings'))
        self.assertEqual(settings_processor(Mock())['settings'], settings)

    def test_settings_processor_on_view(self):
        response = self.app.get(reverse('home'))
        self.assertTrue('settings' in response.context)
        self.assertEqual(response.context['settings'], settings)