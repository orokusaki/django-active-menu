from django.conf import settings
from django.core.urlresolvers import resolve


class MenuItem(object):
    """
    A menu item representing a named URL and an optional parent menu item.
    """
    def __init__(self, view_name, parent=None):
        """
        Sets the view name and parent for upstream use.
        """
        self.view_name = view_name
        self.parent = parent

    def __repr__(self):
        """
        Returns a basic representation with the view name.
        """
        return u'<MenuItem {v}>'.format(v=self.view_name)


class Menu(object):
    """
    A registry of menu items providing helper methods.
    """
    def __init__(self):
        """
        Set's up an empty registry.
        """
        self._registry = {}

    def register(self, menu_item):
        """
        Adds a menu item to the registry. Raises a menu error, if the menu item
        is already in the registry.
        """
        # Get the view name
        view_name = menu_item.view_name

        # Enesure the menu item isn't already registered
        if menu_item.view_name in self._registry:
            raise MenuError(
                u'{v} already registered'.format(v=menu_item.view_name)
            )

        # Add the menu item to the registry dict as the view name
        self._registry[view_name] = menu_item

    def get_item(self, view_name):
        """
        Returns the menu item matching the provided view name from the menu's
        registry. Raises a menu error, if the view name isn't in the registry.
        """
        try:
            return self._registry[view_name]
        except KeyError:
            raise MenuError(u'Menu item "{v}" not found'.format(v=view_name))

    def get_ancesters(self, menu_item):
        """
        Returns all ancester menu items of the provided menu item in bottom-up
        order.
        """
        ancesters = []

        # Walk up the tree adding each menu item to the list of ancestors
        current_node = menu_item
        while current_node.parent is not None:
            current_node = current_node.parent
            ancesters.append(current_node)

        return ancesters

    def isactive(self, request, view_name):
        """
        Returns whether the menu item represented by the provided view name or
        any of its parent menu items represent the provided request's view.
        """
        # Resolve the request
        resolver_match = resolve(request.path_info)

        # Get the provided request's view name
        request_view_name = resolver_match.view_name

        # Return True, if the view name matches the request's view name
        if view_name == request_view_name:
            return True

        # Check whether to use registration (defaulting to True)
        if not getattr(settings, 'ACTIVE_MENU_USE_REGISTRATION', True):
            return False  # Short circuit, registration not used

        # Get the menu item for the provided view name
        menu_item = self.get_item(view_name)

        # Get the provided request's menu item or return False
        try:
            request_menu_item = self.get_item(request_view_name)
        except MenuError:
            return False

        # Return whether the menu item matching the provided view name is in
        # the list of ancestors of the provided request's menu item
        return menu_item in self.get_ancesters(request_menu_item)


class MenuError(Exception):
    """
    Any exception that occurs through incorrect usage of active menus.
    """
    pass
