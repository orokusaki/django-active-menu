from django import template

from active_menu.utils import isactive


# Create a template library
register = template.Library()


@register.simple_tag(takes_context=True, name='active_class')
def active_class(context, view_name):
    """
    Returns ' class="active"' when the current view's name, including its
    namespace, matches the provided view name, else returns empty unicode.
    """
    # Get the request from the context.
    request = context['request']

    # Return the active class, if the view name represents the request's view
    if isactive(request, view_name):
        return u' class="active"'

    return u''
