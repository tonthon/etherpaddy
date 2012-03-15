# -*- coding: utf-8 -*-
# * File Name : populate.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 11-01-2012
# * Last Modified : mer. 11 janv. 2012 16:30:37 CET
#
# * Project :
#
import os
import sys

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging

from etherpadpadlist.models import initialize_sql

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, etherpad-padlist)
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
