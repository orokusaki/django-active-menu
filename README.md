Django Active Menu
==================

A library providing a template tag for adding class="active" to active view
links (or whose parents are active) for Django 1.5+

Usage
-----

Optionally, add `'active_menu'` to `settings.INSTALLED_APPS`. This isn't required,
and there are no models included in Active Menu. This simply allows you to use
`{% load active_menu_tags %}` in your templates. You can use instead use
`add_to_builtins('active_menu.templatetags.active_menu_tags')`, if desired.

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

The above example results in the following when either of the `account` or
`change_password` menu items are active, allowing you to keep your top level
menu items highlighted while child views are active as well. There isn't a
logical limit to the depths at which you can nest your views and there isn't
any magic. Active Menu simply figures out whether a given view name represents
an active link based on what you've registered using the `menu_item` function.

```html
<p>
    <a class="active" href="/some/path/">Change Password</a>
</p>
```

The above example results in the following when neither the `change_password`
nor the `account` menu items are active, using the above example.

```html
<p>
    <a href="/some/path/">Change Password</a>
</p>
```

### Pro Tip

If you don't care about nesting, but you want the tag to add the active class
when a view name matches the *current * request's view name, you can skip the
registration step.
