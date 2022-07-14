from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,50}$',
        [
            'password must contain 1 number(0 - 9)',
            'password must contain 1 uppercase letters',
            'password must contain 1 lowercase letters',
            ' password must contain 1 non - alpha numeric number',
            ' password is 8 - 50 characters with no space'
        ]
    )
    NAME = (
        r'^[a-zA-Z]{2,100}$',
        'only letters min 2 max 100 ch'
    )
    PHONE = (
        r'^0[95687]{1}\d{8}$',
        'Invalid phone number'
    )
    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
