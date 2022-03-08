from django import template
from freelance.models import *

register = template.Library()

@register.simple_tag(name='get_task_info')
def get_categories():
    return Task.objects.all()