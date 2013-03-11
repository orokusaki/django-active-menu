from active_menu.menu import MenuItem, Menu


# A default menu (similar to contrib.admin's default admin site - make your own
# instance, or multiple, if you choose)
default_menu = Menu()

# Method alias for the default menu's isactive method
isactive = default_menu.isactive


def menu_item(view_name, parent=None):
    """
    Returns a new menu item instance and registers it with the default menu.
    """
    item = MenuItem(view_name, parent)
    default_menu.register(item)
    return item
