from enum import Enum

class StudentRole(Enum):
    NOT_GRADUATED = 1
    GRADUATED = 2

    @property
    def value(self):
        return self.value