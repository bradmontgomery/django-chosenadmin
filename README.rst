django-chosenadmin
==================

Adds the `Chosen.js <http://harvesthq.github.io/chosen/>`_ plugin to Select and
Multi-select elements in Django's admin.


About
-----

This app is kind of a hack. It uses middleware to rewrite the Response content,
adding in CSS and JavaScript where appropriate. This may or may not break
anything else you've got.

This is based on Chosen v1.4.2 and only supports jQuery.


Setup
-----

1. Add ``chosenadmin`` to your ``INSTALLED_APPS``.
2. Add ``'chosenadmin.middleware.ChosenAdminMiddleware'`` to the top of your
   ``MIDDLEWARE_CLASSES``

