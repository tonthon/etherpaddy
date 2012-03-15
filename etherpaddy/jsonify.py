# -*- coding: utf-8 -*-
# * File Name : jsonify.py
#
# * Copyright (C) 2010 Gaston TJEBBES <g.t@majerti.fr>
# * Company : Majerti ( http://www.majerti.fr )
#
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 13-02-2012
# * Last Modified :
#
# * Project :
#
import decimal
import datetime

def jsonify(obj):
    """
        Generic function for jsonifying an object
    """
    if is_saobject(obj):
        return jsonify_saobject(obj)
    elif is_decimal(obj):
        return jsonify_decimal(obj)
    elif is_datetime(obj):
        return jsonify_datetime(obj)
    elif is_explicit(obj):
        return jsonify_explicit(obj)
    elif is_list(obj):
        return [jsonify(o) for o in obj]
    return obj

def is_saobject(obj):
    return hasattr(obj, '_sa_class_manager')

def is_decimal(obj):
    return isinstance(obj, decimal.Decimal)

def is_explicit(obj):
    return hasattr(obj, '__json__')

def is_datetime(obj):
    return isinstance(obj, (datetime.datetime, datetime.date))

def is_list(obj):
    return isinstance(obj, list) or isinstance(obj, tuple)

def jsonify_saobject(obj):
    props = {}
    for key in obj.__dict__:
        if not key.startswith('_sa_'):
            props[key] = jsonify(getattr(obj, key))
    return props

def jsonify_datetime(obj):
    """JSONify datetime and date objects."""
    #TODO : format date in readable format
    return obj.strftime("%d-%m-%Y %H:%M:%S")

def jsonify_decimal(obj):
    """JSONify decimal objects."""
    return float(obj)

def jsonify_explicit(obj):
    """JSONify objects with explicit JSONification method."""
    return obj.__json__()
