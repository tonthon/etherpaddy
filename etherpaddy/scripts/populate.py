# -*- coding: utf-8 -*-
# * File Name : populate.py
#
# * Copyright (C) 2012 Majerti <tech@majerti.fr>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 11-01-2012
# * Last Modified : ven. 16 mars 2012 00:33:58 CET
#
# * Project :
#
import os
import sys

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging

from etherpaddy.models import initialize_sql

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
    settings = get_appsettings(config_uri, etherpaddy)
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
