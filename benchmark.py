''' PyRoulette - benchmark.py '''
from itertools import groupby
from random import random
from timeit import timeit



def my_algorithm() -> tuple[int, int]:
    ''' This is the algorithm i came up with '''
    results = [random() >= 0.5 for _ in range(100)]
    max_reds: list[int] = []
    max_blacks: list[int] = []
    for value, sequence in groupby(results):
        if value:
            max_reds.append(sum(sequence))
        else:
            max_blacks.append(len(list(sequence)) - sum(sequence))
    return max(max_reds), max(max_blacks)


def your_algorithm() -> tuple[int, int]:
    ''' Put your code here... '''
    pass


if __name__ == '__main__':
    for i in range(5):
        my_time = timeit(my_algorithm)
        your_time = timeit(your_algorithm)
        best = "my_algorithm" if my_time <= your_time else "your_algorithm"
        print(f"[{i+1}/5] {my_time=}, {your_time=}, {best=}")
