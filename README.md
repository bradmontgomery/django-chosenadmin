django-chosenadmin
==================

Adds the [Chosen.js](http://harvesthq.github.io/chosen/) plugin to `<select>`
and `<select multiple>` elements in Django's admin.


Setup
-----

1. Install with `pip install django-chosenadmin`.
2. Add `chosenadmin` to your `INSTALLED_APPS`.
3. Add `'chosenadmin.middleware.ChosenAdminMiddleware'` to your list of
   `MIDDLEWARE` in your project.


About
-----

This app is kind of a hack. It uses middleware to rewrite the Response content,
adding in CSS and JavaScript where appropriate. This may or may not break
anything else you've got.

However, it's pretty easy to install, and once installed, you don't have to
do anything special in the admin to see it work.

This is based on Chosen v1.8.2 and only supports jQuery. Last tested with Django
1.11 (it uses new-style middleware) with python 3.6.
