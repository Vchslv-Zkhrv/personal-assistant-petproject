from enum import Enum as _Enum


class RotationType(_Enum):
    weekday = "weekday"
    monthday = "monthday"
    periodic = "periodic"


class Weekday(_Enum):
    monday = 1
    tuesday = 2
    wednesday = 3
    thursday = 4
    friday = 5
    saturday = 6
    sunday = 7
