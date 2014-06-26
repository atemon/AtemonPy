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
from .http import (BadRequest,
                   Unauthorized,
                   Forbidden,
                   ResourceNotFound,
                   MethodNotAllowed,
                   InternalServerError,
                   NotImplemented as http_NotImplemented,
                   PaymentRequired
                   )


def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_all_exception(exception):
        raise BasicException(exception=exception)

    @app.errorhandler(BasicException)
    def handle_atemon_exception(exception):
        return exception.jsonify()

    @app.errorhandler(400)
    def atemon_flask_400(exception):
        raise BadRequest(exception=exception)

    @app.errorhandler(401)
    def atemon_flask_401(exception):
        raise Unauthorized(exception=exception)

    @app.errorhandler(402)
    def atemon_flask_402(exception):
        raise PaymentRequired(exception=exception)

    @app.errorhandler(403)
    def atemon_flask_403(exception):
        raise Forbidden(exception=exception)

    @app.errorhandler(404)
    def atemon_flask_404(exception):
        raise ResourceNotFound(exception=exception)

    @app.errorhandler(405)
    def atemon_flask_405(exception):
        raise MethodNotAllowed(exception=exception)

    @app.errorhandler(500)
    def atemon_flask_500(exception):
        raise InternalServerError(exception=exception)

    @app.errorhandler(501)
    def atemon_flask_501(exception):
        raise http_NotImplemented(exception=exception)
