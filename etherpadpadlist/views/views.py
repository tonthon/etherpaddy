# -*- coding: utf-8 -*-
# * File Name : views.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : mer. 11 janv. 2012
# * Last Modified : jeu. 15 mars 2012 15:43:43 CET
#
# * Project : etherpad-padlist
#

from pyramid.view import view_config

from etherpadpadlist.models.model import get_all_pads
from etherpadpadlist.json import jsonify
#from etherpadpadlist.models import DBSESSION
# DBSESSION is used to access database:
#ex :
#    session = DBSESSION()
#    users = session.query(User).all()

@view_config(route_name='index', renderer='index.mako')
def default_index(request):
    """
        Return only a title for the page
    """
    return dict(title="Default page for pyramid projects from Majerti")

@view_config(route_name='pads', renderer='json', request_method='GET', xhr=True)
@view_config(route_name='pads', renderer='padlist.mako', request_method='GET')
def pads(request):
    """
        Returns the list of all users
    """
    all_pads = get_all_pads()
    if request.is_xhr:
        return_datas = [jsonify(pad) for pad in all_pads]
    else:
        return_datas = {'title':"List of all our pads", "pads":pads}
    return return_datas
