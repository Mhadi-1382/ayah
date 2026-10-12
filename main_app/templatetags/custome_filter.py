from django import template
from persiantools.jdatetime import JalaliDateTime

register = template.Library()

@register.filter
def to_jalali(value):
    if value:
        return JalaliDateTime(value).strftime('%Y-%m-%d %H:%M')
    return ''
