from sorokin_test2.core.models import Request
from django.conf import settings
import re
import json


class RequestStatistic(object):

    def path_is_valid(self, path):
        pattern = re.compile(r'^({0}|{1})|/favicon\.ico.*'.format(
                                                      settings.MEDIA_URL,
                                                      settings.STATIC_URL))
        if not re.match(pattern, path):
            return True
        return False

    def process_response(self, request, response):
        if self.path_is_valid(request.path):
            params = request.GET if request.method == 'GET' else request.POST
            Request.objects.create(path=request.path,
                                   status_code=response.status_code,
                                   method=request.method,
                                   params=json.dumps(params))
        return response
