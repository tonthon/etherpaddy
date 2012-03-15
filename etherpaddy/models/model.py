# -*- coding: utf-8 -*-
# * File Name : model.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : mer. 11 janv. 2012
# * Last Modified : ven. 16 mars 2012 00:33:05 CET
#
# * Project : etherpaddy
#
"""
    Model to wrap the existing database
"""
from etherpaddy.models import DBBASE, DBSESSION

class StoreItem(DBBASE):
    """
        The store table is the unique db table
    """
    __tablename__ = 'store'
    __table_args__ = {'autoload':True}

    def get_name(self):
        return self.key[4:]

def get_all_pads():
    """
        Return all existing pads from the database
    """
    padregex = "^pad:{1}[a-zA-Z0-9]+$"
    return DBSESSION().query(StoreItem).filter(StoreItem.key.op('regexp')(padregex))
