from enum import Enum


class RegEx(Enum):
    BRAND = (r'^[a-zA-Z]{2,100}$', 'Only letters min 2 max 100 ch')

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
