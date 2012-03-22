# -*- coding: utf-8 -*-
# * File Name : api.py
#
# * Copyright (C) 2010 Gaston TJEBBES <g.t@majerti.fr>
# * Company : Majerti ( http://www.majerti.fr )
#
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 22-03-2012
# * Last Modified :
#
# * Project :
#
"""
    All the api exchange stuff
"""
import os
import json
import urllib
import urllib2

from urllib2 import URLError

from pyramid.threadlocal import get_current_registry

API_VERSION = "1"
TIMEOUT = 15

def get_api_infos():
    """
        Load api configuration
    """
    settings = get_current_registry().settings
    host = settings['etherpaddy.host']
    apikey = settings['etherpaddy.apikey']
    apiurl = os.path.join(host, 'api', API_VERSION)
    return apiurl, apikey

def build_post_args(padid, apikey):
    """
        return escaped post_args
    """
    padid = padid.encode('utf-8')
    post_args = {'padID': padid, 'apikey':apikey}
    return urllib.urlencode(post_args, True)

def delete_pad(padid):
    """
        Delete a pad
    """
    try:
        apiurl, apikey = get_api_infos()
        delurl = os.path.join(apiurl, 'deletePad')
        data = build_post_args(padid, apikey)
        opener = urllib2.build_opener()
        request = urllib2.Request(url=delurl, data=data)
        response = opener.open(request, timeout=TIMEOUT)
        result = response.read()
    except KeyError:
        return dict(code=1,
                message="Missing configuration datas")
    except URLError:
        return dict(code=1,
                    message="Unable to join etherpad-lite's api, \
 check your configuration and your network connection")
    result = json.loads(result)
    if result is None:
        return dict(code=1,
                    message="Maybe the pad has been succesfully deleted")
    return result
