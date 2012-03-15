# -*- coding: utf-8 -*-
# * File Name : views.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : mer. 11 janv. 2012
# * Last Modified : ven. 16 mars 2012 00:30:10 CET
#
# * Project : etherpad-padlist
#
"""
    Main views for etherpad-lite
"""

from pyramid.view import view_config

from etherpadpadlist.models.model import get_all_pads
from etherpadpadlist.jsonify import jsonify

@view_config(route_name='index', renderer='index.mako')
def default_index(request):
    """
        Return only a title for the page
    """
    return dict(title="Welcome on Etherpaddy")

@view_config(route_name='pads', renderer='json', request_method='GET', xhr=True)
@view_config(route_name='pads', renderer='padlist.mako', request_method='GET')
def pads(request):
    """
        Returns the list of all users
    """
    all_pads = get_all_pads()
    if request.is_xhr:
        return_datas = [jsonify(p) for p in all_pads]
    else:
        return_datas = {'title':"List of all our pads", "pads":all_pads}
    return return_datas

@view_config(route_name='pad', renderer='padedit.mako', request_method='GET')
def pad(request):
    """
        View to embed etherpad lite in an iframe
    """
    padid = request.matchdict.get('padid')
    return dict(padid=padid, title='')

@view_config(route_name='padnew', renderer='addpad.mako', request_method='GET')
def newpad(request):
    """
        Returns the pad add form
    """
    return dict(title='Add a new pad')
