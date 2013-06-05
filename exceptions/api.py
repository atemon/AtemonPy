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

from .http import (BadRequest,
                   Unauthorized,
                   Forbidden,
                   ResourceNotFound,
                   MethodNotAllowed,
                   InternalServerError,
                   NotImplemented as http_NotImplemented,
                   PaymentRequired
                   )


class APIException(BasicException):
    pass


class InputValidationError(BadRequest):
    api_code = 100
    api_message = 'Input Validation Error'


class AuthenticationRequired(Unauthorized):
    api_code = 101
    api_message = 'Authentication required'


class APIResourceNotFound(ResourceNotFound):
    api_code = 104
    api_message = "API resource not found"


class APIMethodNotAllowed(MethodNotAllowed):
    api_code = 104
    api_message = "API method not allowed"
