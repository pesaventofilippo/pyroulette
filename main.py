from random import random
from itertools import groupby
from operator import itemgetter
from multiprocessing import Pool


def spin_times(spins: int) -> tuple:
    """
    Simulate a single round with N spins, and determine the longest sequence for both outcomes

    :param spins: The number of spins (coin flips) per round
    :return: Longest sequence of 1s, longest sequence of 0s
    """
    results = [random() >= 0.5 for _ in range(spins)]
    max_reds = []
    max_blacks = []
    for value, sequence in groupby(results):
        if value:
            max_reds.append(sum(sequence))
        else:
            max_blacks.append(len(list(sequence)) - sum(sequence))
    return max(max_reds), max(max_blacks)


def run_batch(rounds: int=100, spins_per_round: int=100, threads: int=1) -> tuple:
    """
    Run many rounds concurrently with separate threads (GIL-indipendent)

    :param rounds: Number of simulations (rounds) to run
    :param spins_per_round: The number of spins (coin flips) per round
    :param threads: Number of threads to spawn for the simulation
    :return: The longest sequence of 1s and 0s from all simulations
    """
    with Pool(threads) as pool:
        results = pool.map(spin_times, [spins_per_round]*rounds, chunksize=100000)
    longest_red_sequence = max(results, key=itemgetter(0))[0]
    longest_black_sequence = max(results, key=itemgetter(1))[1]
    return longest_red_sequence, longest_black_sequence


if __name__ == '__main__':
    from sys import argv
    from time import time

    rounds = 100
    spins_per_round = 100
    threads = 1
    file = None
    for i in range(1, len(argv)):
        if argv[i] in ["-r", "--rounds"]:
            rounds = int(argv[i+1])
        elif argv[i] in ["-s", "--spins", "--spins-per-round"]:
            spins_per_round = int(argv[i+1])
        elif argv[i] in ["-t", "-c", "--threads", "--cpu"]:
            threads = int(argv[i+1])
        elif argv[i] in ["-o", "--out"]:
            file = str(argv[i+1])

    t_start = time()
    result = run_batch(rounds=rounds, spins_per_round=spins_per_round, threads=threads)
    t_end = time()
    text = f"--- SIMULATION ENDED ---\n" \
           f"Rounds: {rounds}\n" \
           f"Spins per round: {spins_per_round}\n" \
           f"\n" \
           f"Longest run of 'reds'/'heads': {result[0]}\n" \
           f"Longest run of 'blacks'/'tails': {result[1]}\n" \
           f"Total time of simulation: {round(t_end-t_start, 1)}s\n"
    print(text)
    if file:
        with open(file, "w") as out:
            if out.writable():
                out.write(text)
