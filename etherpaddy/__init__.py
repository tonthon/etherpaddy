# -*- coding: utf-8 -*-
# * File Name : __init__.py
#
# * Copyright (C) 2010 Gaston TJEBBES <tonthon21@gmail.com>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 11-01-2012
# * Last Modified : ven. 16 mars 2012 18:24:47 CET
#
# * Project : etherpaddy
#
"""
    Main file of the project
"""

from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from etherpaddy.models import initialize_sql

def main(global_config, **settings):
    """
        Main function : returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    config = Configurator(settings=settings)
    config.add_static_view('static', 'etherpaddy:static',
                                            cache_max_age=3600)
    config.add_route('index', '/')
    # REST API
    # using the four HTTP methods (POST, GET, PUT, DELETE),
    # translating them in (add, get, update, delete)
    # and the two following routes,
    # we can get a very clean REST API
    config.add_route("pads", "/pads")
    config.add_route("padnew", "/pads/new")
    config.add_route("genpadname", "/pads/randomid")
    config.add_route("pad", "/pads/{padid}")
    config.add_route("etherpad", settings['etherpaddy.ethpath'])

    config.scan('etherpaddy')
    return config.make_wsgi_app()
