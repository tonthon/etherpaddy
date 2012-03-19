etherpaddy
==========

Etherpaddy is a `Pyramid`_ application wrapping etherpad-lite to allow simple actions on etherpad-lite's pads.

Who is it for ?
---------------

Etherpaddy has been created to allow a simple use of etherpad-lite inside our team.
It doesn't use any groups or sessions.

Features
--------

Etherpaddy provides
    - Pad list window
    - Custom Pad add page
    - Custom Editing page with link to fullscreen mode and deleting mode
    - Etherpad-lite custom menu item to allow going back to the pad list from the fullscreen mode

Getting Started
---------------

`Pyramid`_ is a python web framework.
Etherpaddy is also using sqlalchemy and `Twitter Bootstrap` for design.

Installation
------------

Thoses installation tips are GNU/Linux oriented, but it shouldn't be a problem to install it on other plateforms.

First of all, we suppose you have :
    - An etherpad-lite installed and running on your server (or a foreign one).
      See `Etherpad-lite on github`_
    - python-setup-tools and python-virtualenv (apt-get install or yum install or ...)
    - An apache webserver with mod_wsgi, mod_proxy, mod_proxy_http and auth_pam

Install etherpaddy
~~~~~~~~~~~~~~~~~~

Create a virtualenv, activate, download from github and install:

.. code-block:: bash

    cd /var/www
    virtualenv --no-site-packages env
    cd env
    source bin/activate
    git clone git://github.com/tonthon/etherpaddy.git
    cd etherpaddy
    python setup.py develop

Configure Etherpaddy
~~~~~~~~~~~~~~~~~~~~

The etherpaddy contains a production.ini file that you should customize to fit your sql configuration.
The sqlalchemy.url should be modified to allow connection on the etherpad-lite database, since the etherpaddy database is utf8_bin, you need to add some specific attributes.
Your configuration should look like ;
.. code-block::

    sqlalchemy.url=mysql://user:pass@localhost/dbname?charset=utf8&use_unicode=0
    sqlalchemy.encoding=UTF8
    sqlalchemy.convert_unicode = True

The filelog handler should also be modified to set the logfile path and a logrotate configuration should be added.

Customising Etherpad-lite
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to add a simple button allowing to go back to etherpaddy from inside etherpad-lite (when in fullscreen mode),
you should place etherpaddy/etherpad-lite/static/custom/pad.js in etherpad-lite/static/custom/ (don't forget to set the rights to your etherpad user if needed).

Configure Apache
~~~~~~~~~~~~~~~~

Etherpaddy comes with a pyramid.wsgi file and a sample apache configuration.
The pyramid.wsgi file should be placed in the env directory created here above (with the virtualenv command).

The sample configuration :
    - Add pam authentication on /
    - Reverseproxy etherpad-lite (asserting it runs on the same server on the port 9001)
    - Serves our pyramid app on / through wsgi
    - Serves static files on /static/

The apache configuration naturally needs some customisation and should be used as any apache conf (placed into /.../apache2/sites-available/ and a2ensite).

You need to manually create a directory under your env/etherpaddy directory and add write access for www-data on it :

.. code:: bash

    mkdir -p /var/www/env/etherpaddy/mako_compiled_templates
    chown -R www-data:www-data /var/www/env/etherpaddy/mako_compiled_templates


Notes on mysql and virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mysql-python is sometimes a little tricky to install. Since it's a compiled library, it needs some os-wide dependencies.
For example, on Debian, you'll need to install python-dev libmysqlclient-dev and build-essential.

.. _Etherpad-lite on github: https://github.com/Pita/etherpad-lite
.. _Pyramid: http://www.pylonsproject.org/
.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/
