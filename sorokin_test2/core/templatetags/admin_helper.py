from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(obj):
    return reverse("admin:{0}_{1}_change".format(obj._meta.app_label,
                             obj.__class__.__name__.lower()), args=[obj.id])
