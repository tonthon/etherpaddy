# -*- coding: utf-8 -*-
# * File Name : views.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : mer. 11 janv. 2012
# * Last Modified : jeu. 22 mars 2012 12:03:31 CET
#
# * Project : etherpaddy
#
"""
    Main views for etherpad-lite
"""
import string
import random

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_path

from etherpaddy.models.model import get_all_pads
from etherpaddy.jsonify import jsonify
from etherpaddy.api import delete_pad

def gen_random():
    """
        Returns a random string composed with digits and characters
    """
    rand = ''.join(random.choice(string.ascii_letters + string.digits)
                                                        for x in range(10))
    return "random_" + rand

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

@view_config(route_name='pad', renderer='json',
                                    request_method='DELETE')
def deletepad(request):
    """
        Delete a pad
    """
    padid = request.matchdict.get('padid')
    return delete_pad(padid)

@view_config(route_name='genpadname', renderer='json', request_method='GET')
def genpadname(request):
    """
        Redirect to a new pad with a random name
    """
    all_pads = [p.get_name() for p in get_all_pads()]
    name = gen_random()
    while name in all_pads:
        name = gen_random()
    return HTTPFound(route_path('pad', request, padid=name))
