from django import template

register = template.Library()

@register.filter
def prefix(value):
    """
    Returns the substring before the first underscore.
    If no underscore is present, returns the original string.
    Example: 'blogue_article_1' -> 'blogue'
    """
    if not isinstance(value, str):
        return value
    return value.split('_')[0]
