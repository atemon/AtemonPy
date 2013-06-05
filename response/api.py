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

from ..lib import FixedDictionary


class BaseResponse(FixedDictionary):

    version = '0.0.1'

    def __init__(self, data=None):
        FixedDictionary.__init__(self, {'http_code': 200,
                                        'http_message': 'Success',
                                        'api_code': '200',
                                        'api_message': 'Success',
                                        'data': data,
                                        'version': self.version
                                        })

    def return_exception(self, exception):
        self.merge(exception)
