# -*- coding: utf-8 -*-
#
# Copyright 2014 Agile Technology Engineers Monastery - ATEMON
#
# Git Hub: https://github.com/atemon
# Twitter: https://twitter.com/atemonastery
#
# This file is part of atemon library.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import simplejson

from api import BaseResponse
from ..exceptions import BasicException, InvalidOutput
from ..lib import FixedDictionary

def jsonified_response(f):
    def wrapper(*args, **kwargs):
        rv = f(*args, **kwargs)
        try:
            if isinstance(rv, FixedDictionary):
                return rv.jsonify()
            else:
                try:
                    return simplejson.dump()
                except:
                    raise
        except BasicException as be:
            return be.jsonify()
        except Exception as e:
            raise e

    return wrapper
