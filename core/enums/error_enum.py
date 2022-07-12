from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ({'details': 'Invalid or expired token'}, status.HTTP_403_FORBIDDEN)

    def __init__(self, msg, code=status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.code = code
