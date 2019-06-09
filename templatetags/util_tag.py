from django import template
register = template.Library()

@register.filter(name="formatImageUrl")
def formatImageUrl(value):
    return value.replace('res.cloudinary.com/hqunnkpk8/image/upload/', 'res.cloudinary.com/hqunnkpk8/image/upload/f_auto/')