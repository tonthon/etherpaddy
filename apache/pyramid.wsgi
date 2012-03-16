import os
from pyramid.paster import get_app
HERE = os.path.dirname(__file__)
APP_INIFILE = os.path.join(HERE, 'etherpaddy', 'production.ini')
application = get_app(APP_INIFILE, 'main')
