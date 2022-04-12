import locale
from django import template

register = template.Library()

@register.filter
def currency(value):
        pass
