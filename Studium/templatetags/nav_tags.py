from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, view_name):
    request = context['request']
    if request.path == reverse(view_name):
        return 'active'
    return ''