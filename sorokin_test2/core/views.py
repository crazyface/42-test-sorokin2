from django.views.generic.list import ListView
from sorokin_test2.core.models import Request


class RequestView(ListView):
    model = Request

    def get_queryset(self):
        return self.model.objects.all()[:10]