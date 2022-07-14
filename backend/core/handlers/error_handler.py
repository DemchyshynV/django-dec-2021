from rest_framework.response import Response
from rest_framework.views import exception_handler

from core.enums.error_enum import ErrorEnum


def custom_error_handler(exc: Exception, content: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error
    }

    response = exception_handler(exc, content)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        function = handlers[exc_class]
        return function(exc, content)

    return response


def _jwt_validate_error(exc: Exception, content: dict) -> Response:
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)
