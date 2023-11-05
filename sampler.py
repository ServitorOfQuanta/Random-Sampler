from secrets import randbelow
from typing import Sequence
import argparse


def sample(pool_m: Sequence, n: int):
    length = len(pool_m)
    samples = []
    if n > length or n < 0:
        raise AssertionError(
            "The number of samples requested either exceeds the number of the samples in the pool or is negative."
        )
    elif n == length:
        return pool_m
    elif n == 0:
        return []
    places = list(range(length))
    for _ in range(n):
        max_place = len(places)
        place = randbelow(max_place)
        sample_place = places[place]
        samples.append(pool_m[sample_place])
        places.pop(place)
    return samples


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get a random sample from a pool m of number n"
    )

    parser.add_argument("--m", nargs="+", help="Pool m of population to sample from")
    parser.add_argument("--n", type=int, help="Number of samples requested")

    input_args = parser.parse_args()

    print(sample(input_args.m, input_args.n))
