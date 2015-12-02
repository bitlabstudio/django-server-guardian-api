Django Server Guardian API
============

API offering health metrics for the ``django-server-guardian`` app.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-server-guardian-api

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-server-guardian-api.git#egg=server_guardian_api

TODO: Describe further installation steps (edit / remove the examples below):

Add ``server_guardian_api`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'server_guardian_api',
    )

Add the ``server_guardian_api`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^server-guardian-api/', include('server_guardian_api.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load server_guardian_api_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate server_guardian_api


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-server-guardian-api
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.6 and Django 1.7) and run the tests against both
environments.
