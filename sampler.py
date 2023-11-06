from secrets import randbelow
from typing import Sequence
import argparse


def sample(pool_m: Sequence, n: int):
    """This function performs a random sample selection of size n from a pool (pool_m) without replacement.

    Args:
        pool_m (Sequence): Any sequence of objects that we select from.
        n (int): Any non-negative integer lower than the length of pool_m. This represents the number of draws that will be made.

    Raises:
        AssertionError: This function will throw an assertion error if n is found to be negative or higher than the length of pool_m

    Returns:
        list: _description_
    """
    if not isinstance(pool_m, Sequence):
        raise TypeError(
            "pool_m must be a list, tuple, or range"
        )
    if not isinstance(n, int):
        raise TypeError(
            "n must be an integer"
        )

    length = len(pool_m)
    samples = []

    if n > length or n < 0:
        raise AssertionError(
            "The number of samples requested either exceeds the number of the samples in the pool or is negative."
        )
    elif n == length:
        return list(pool_m)
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

    if not (input_args.m or input_args.n):
        parser.error("No pool or number given, please call with both --m and --n")

    print(sample(input_args.m, input_args.n))
