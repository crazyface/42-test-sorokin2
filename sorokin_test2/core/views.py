from django.views.generic.list import ListView
from sorokin_test2.core.models import Request
from django.core.urlresolvers import reverse


class RequestView(ListView):
    model = Request

    def is_reversed(self):
        if self.kwargs.get('order'):
            return True
        return False

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.is_reversed():
            qs = qs.order_by('priority', '-created_at')
        else:
            qs = qs.order_by('-priority', '-created_at')
        return qs[:10]

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        if self.is_reversed():
            url = reverse('core:requests')
        else:
            url = reverse('core:requests', kwargs={'order': 'reverse/'})
        context['order_url'] = url
        return context