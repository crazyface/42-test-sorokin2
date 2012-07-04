"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from sorokin_test2.accounts.models import Profile
from sorokin_test2.core.models import Request, DbActivity
from django.conf import settings
from sorokin_test2.core.middlewares import RequestStatistic
from sorokin_test2.core.contextprocessors import settings_processor
from django.test.client import RequestFactory
from mock import Mock, patch
from sorokin_test2.core.templatetags.admin_helper import edit_link
from django.contrib.auth.models import User
from sorokin_test2.core.management.commands.show_models import Command
from django.core.management import call_command
from django.contrib.contenttypes.models import ContentType

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


class EditLinkTestCase(WebTest):
    def test_tag(self):
        obj = Profile.objects.get(id=1)
        self.assertEqual(reverse('admin:accounts_profile_change',
                                                                args=[obj.id]),
                         edit_link(obj))
        user = User.objects.get(id=1)
        self.assertEqual(reverse('admin:auth_user_change', args=[user.id]),
                         edit_link(user))


class ShowModelsCommandTestCase(WebTest):
    class DummyStdout:
        def __init__(self):
            self.out = ''

        def write(self, output):
                self.out += output

    def test_command_with_params(self):
        stdout = self.DummyStdout()
        call_command('show_models', 'accounts.Profile',**{'stdout': stdout,
                                              'stderr': self.DummyStdout()})
        self.assertTrue('accounts.Profile' in stdout.out)
        self.assertFalse('core.Request' in stdout.out)

    def test_command_without_params(self):
        stdout = self.DummyStdout()
        call_command('show_models', **{'stdout': stdout,
                                       'stderr': self.DummyStdout()})
        self.assertTrue('accounts.Profile' in stdout.out)
        self.assertTrue('core.Request' in stdout.out)


class Signal_HandlerTestCase(WebTest):
    
    def setUp(self):
        self.ctype = ContentType.objects.get_for_model(Profile)
        WebTest.setUp(self)

    def test_create(self):
        obj = Profile.objects.get(id=1)
        obj.pk = None
        obj.save()
        qs = DbActivity.objects.filter(model=self.ctype, obj_pk=obj.pk,
                                       action='create')

    def test_update(self):
        obj = Profile.objects.get(id=1)
        obj.first_name = 'test'
        obj.save()
        qs = DbActivity.objects.filter(model=self.ctype, obj_pk=obj.pk,
                                       action='update')
        self.assertTrue(qs.exists())

    def test_delete(self):
        obj= Profile.objects.get(id=1)
        pk = obj.pk
        obj.delete()
        qs = DbActivity.objects.filter(model=self.ctype, obj_pk=pk,
                                       action='delete')
        self.assertTrue(qs.exists())

