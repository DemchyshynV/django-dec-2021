from enum import Enum


class RegEx(Enum):
    NAME = (r'^[a-zA-Z]{1,20}$', 'Only Letters min 1 max 20 ch')

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
