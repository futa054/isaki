from django import template
register = template.Library()

@register.filter(name="formatImageUrl")
def formatImageUrl(value):
    return value.replace('image/upload/', 'image/upload/f_auto,q_auto/')