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


class BasicException(Exception, FixedDictionary):
    http_code = 500
    http_message = 'Internal Server Error'
    api_code = 500
    api_message = 'Internal Server Error'

    def __init__(self, message=None, exception=None, **message_dict):

        if isinstance(exception, Exception) and hasattr(exception.message):
            self.api_message = exception.message
        else:
            self.api_message = message or self.api_message

        Exception.__init__(self, self.api_message)
        FixedDictionary.__init__(self, {'http_code': self.http_code,
                                        'http_message': self.http_message,
                                        'api_code': self.api_code,
                                        'api_message': self.api_message,
                                        'data': None,
                                        })

    def set_http_status(self, code, message=''):
        self.http_code = code
        self.http_message = message

    def set_response(self, code, message=''):
        self.api_code = code
        self.api_message = message

    def set_message(self, message):
        self.api_message = message

    def set_exception(self, exception):
        self.api_message = exception.message
