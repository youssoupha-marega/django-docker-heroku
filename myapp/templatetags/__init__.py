from django import template

register = template.Library()

@register.filter
def prefix(value):
    """Retourne tout ce qui est avant le premier _"""
    return value.split("_")[0]
