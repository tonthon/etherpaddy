# -*- coding: utf-8 -*-
# * File Name : model.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : mer. 11 janv. 2012
# * Last Modified : jeu. 15 mars 2012 15:33:53 CET
#
# * Project : etherpad-padlist
#
"""
    Model to wrap the existing database
"""
from etherpadpadlist.models import DBBASE, DBSESSION

class StoreItem(DBBASE):
    """
        The store table is the unique db table
    """
    __tablename__ = 'store'
    __table_args__ = {'autoload':True}

def get_all_pads():
    """
        Return all existing pads from the database
    """
    return DBSESSION().query(StoreItem).filter(StoreItem.key.like('pad:%'))
