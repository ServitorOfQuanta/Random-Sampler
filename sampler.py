from secrets import randbelow
from typing import Sequence

def sample(pool_m: Sequence, n: int):
    length = len(pool_m)
    sample = []
    if n > length or n < 0:
        raise AssertionError("The number of samples requested either exceeds the number of the samples in the pool or is negative.")
    elif n == length:
        return pool_m
    places = range(0, 1, n-1)
    for i in range(0, n):
        place = randbelow(len(places))
        sample.append(pool_m[place])
        places.pop(place)
    return sample