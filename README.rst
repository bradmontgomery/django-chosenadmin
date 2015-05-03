django-chosenadmin
==================

Adds the `Chosen.js <http://harvesthq.github.io/chosen/>`_ plugin to Select and
Multi-select elements in Django's admin.


Setup
-----

1. Install with ``pip install django-chosenadmin``.
2. Add ``chosenadmin`` to your ``INSTALLED_APPS``.
3. Add ``'chosenadmin.middleware.ChosenAdminMiddleware'`` to the top of your
   ``MIDDLEWARE_CLASSES``


About
-----

This app is kind of a hack. It uses middleware to rewrite the Response content,
adding in CSS and JavaScript where appropriate. This may or may not break
anything else you've got.

However, it's pretty easy to install, and once installed, you don't have to
do anything special in the admin to see it work.

This is based on Chosen v1.4.2 and only supports jQuery.

Works with Django 1.8, python 2.7, and python 3.4.
