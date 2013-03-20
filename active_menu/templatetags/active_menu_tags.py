from django import template

from active_menu.utils import isactive


# Create a template library
register = template.Library()


@register.simple_tag(takes_context=True, name='active_class')
def active_class(context, view_name, attribute=True):
    """
    Returns ' class="active"' when the current view's name, including its
    namespace, matches the provided view name, else returns empty unicode.
    """
    # Get the request from the context.
    request = context['request']

    # Return the active class, if the view name represents the request's view
    if isactive(request, view_name):
        if attribute:
            # Return the HTML class attribute
            return u' class="active"'

        # Return the " active" text, including a leading space to avoid the
        # need for anticipatory space in HTML class attributes
        return u' active'

    return u''
