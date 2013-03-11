Django Active Menu
==================

A library providing a template tag for adding class="active" to active view
links (or whose parents are active) for Django 1.5+

Usage
-----

Firstly, add `'active_menu'` to `settings.INSTALLED_APPS`. Don't worry, there
are no models included with Active Menu. This simply allows you to use
`{% load active_menu_tags %}` in your templates.

```python
# urls.py (or anywhere where they'll be run before your views are called)
from active_menu import menu_item


# Create some menu items, providing the view name for each (including their
# namespaces, if applicable)
account = menu_item('account:index')
login = menu_item('account:login', parent=account)
settings = menu_item('account:update_settings', parent=account)
change_password = menu_item('account:change_password', parent=account)
```

Then, use the provided template tag in your templates to set an "active" class
on your links (or whateer you want), based on which links are active.

```html
{% load active_menu_tags %}


<p>
    <a{% active_class 'account:change_password' %} href="{% url 'account:change_password' %}">Change Password</a>
</p>
```

The above example would result in the following when the request was for either
the `account` view or the `change_password` view, allowing you to keep your top
level menu items highlighted when their child views are active.

```html
<p>
    <a class="active" href="/some/path/">Change Password</a>
</p>
```

And the following when neither the `change_password` nor the `account` menu
items are active.

```html
<p>
    <a href="/some/path/">Change Password</a>
</p>
```
