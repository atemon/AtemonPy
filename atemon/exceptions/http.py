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

from .exceptions import BasicException


class HTTPException(BasicException):
    pass


class BadRequest(HTTPException):
    http_code = 400
    http_message = 'Bad request'


class Unauthorized(HTTPException):
    http_code = 401
    http_message = 'Unauthorized'


class PaymentRequired(HTTPException):
    http_code = 402
    http_message = 'Payment Required'


class Forbidden(HTTPException):
    http_code = 403
    http_message = 'Forbidden'


class ResourceNotFound(HTTPException):
    http_code = 404
    http_message = 'Resource not found'


class MethodNotAllowed(HTTPException):
    http_code = 405
    http_message = 'Method not allowed'


class InternalServerError(HTTPException):
    pass


class NotImplemented(HTTPException):
    http_code = 501
    http_message = 'Not implemented'
