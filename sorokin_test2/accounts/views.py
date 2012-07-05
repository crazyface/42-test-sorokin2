# Create your views here.
from django.views.generic.detail import DetailView
from sorokin_test2.accounts.models import Profile
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from sorokin_test2.accounts.forms import ProfileForm
import os
from io import BufferedWriter, FileIO
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import HttpResponseBadRequest, Http404, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template


class GetObjectMixIn(object):
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=1)


class ProfileDetailView(GetObjectMixIn, DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['form'] = ProfileForm()
        return context


class ProfileEditView(GetObjectMixIn, UpdateView):
    model = Profile
    success_url = reverse_lazy('home')
    form_class = ProfileForm

    def ajax(self, form):
        return direct_to_template(self.request, 'accounts/profile_ajax.html',
                                  self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return self.ajax(form)
        return super(ProfileEditView, self).post(request, *args, **kwargs)

def save_upload(uploaded, filename, raw_data):
    """
    raw_data: if True, upfile is a HttpRequest object with raw post data
    as the file, rather than a Django UploadedFile from request.FILES
    """
    IMAGE_UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT,
                                     'photos')
    try:
        filename = os.path.normpath(os.path.join(IMAGE_UPLOAD_PATH, filename))
        with BufferedWriter(FileIO(filename, "wb")) as dest:
            # if the "advanced" upload, read directly from the HTTP request
            # with the Django 1.3 functionality
            if raw_data:
                (dirName, fileName) = os.path.split(filename)
                (fileBaseName, fileExtension) = os.path.splitext(fileName)
                #
                # right here, if fileBaseName is less than n characters, might want to slap on a date just for fun
                #
#                try:
#                    i_can_has_p = Photo.objects.get(title=fileBaseName)
#                    title = fileBaseName + "_" + str(datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))
#                except Photo.DoesNotExist:
                title = fileBaseName
                title_slug = slugify(title)
                p = Profile.objects.get(pk=1)
                p.photo.save(filename, ContentFile(uploaded.read()))
            # if not raw, it was a form upload so read in the normal Django chunks fashion
            else:
                # TODO: figure out when this gets called, make it work to save into a Photo like above
                for c in uploaded.chunks():
                    dest.write(c)
    except IOError:
        # could not open the file most likely
        return False, ''
    return True, p.photo.url

#@csrf_exempt
def ajax_upload(request):
    if request.method == "POST":
        # AJAX Upload will pass the filename in the querystring if it is the "advanced" ajax upload
        if request.is_ajax():
            # the file is stored raw in the request
            upload = request
            is_raw = True
            try:
                filename = request.GET[ 'qqfile' ]
            except KeyError:
                return HttpResponseBadRequest("AJAX request not valid")
        else:
            is_raw = False
            if len(request.FILES) == 1:
                upload = request.FILES.values()[ 0 ]
            else:
                raise Http404("Bad Upload")
            filename = upload.name

    success, url = save_upload(upload, filename, is_raw)
    ret_json = {'success': success, 'url': url}
    return HttpResponse(json.dumps(ret_json), content_type='application/json')
