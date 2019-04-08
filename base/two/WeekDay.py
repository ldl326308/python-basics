# -*- coding:UTF-8 -*-
from enum import Enum, unique


@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(WeekDay.Fri.value)
print(WeekDay.Sun.value)
