# Random Sampler

Random Sampling Exercise

# Setup

Unless you're trying to run the notebook or the unit tests, you shouldn't need to install any packages! animals.py and sampler.py are both ready to run without dependancies.

# Files

## sampler.py

This contains the main function, sample(pool_m, n). This is a function that creates a sample of n objects from a sequence of m objects. This function can either be invoked via the command line in the form passing command line arguments --m and --n, or can be referenced from any other file.

### Assumptions

I made a few assumptions about the context of what I was building, namely:

- My input pool could come in as any sequence, meaning that I could be working with a range or a tuple along with a list. This means that my solution could not edit the pool directly.
- The goal was speed. This is likely to take up a lot of runtime in whatever program it was running for and limiting the amount it took up would be extremely beneficial to the upstream program.
- It was not the point of this exercise to implement a random number generator, just a random sampler. Hence it was okay to limit the scope of this solution to just the sampling behaviour.
- Some degree of determinism was acceptable. Perfect randomness is impossible, but we don't need to be cryptographically secure either given the use case.
- The order of the elements in the sample being chosen is irrelevant. That means that when n = m we can just return the pool unchanged.
- Even though the like users will be other engineers, being harsh about type requirements would be preferred.

## animal.py
This is a cute demonstration of the sample function in action. In it, you go on a trip to the zoo and meet a sample of n number of animals from the zoo's menagerie. It runs from a terminal and has some sassy comments if you try to break it.

## tests_sampler
These are the unit tests, testing both good and bad cases.

## experiments.ipynb
A notebook where I undertook some experiments to test my code against the inbuilt random.sample() function.