from django import template
from freelance.models import *

register = template.Library()

@register.simple_tag(name='getmaincats')
def get_categories():
    return Main_Category.objects.all()