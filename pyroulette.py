''' PyRoulette - main.py '''
from random import random
from itertools import groupby
from operator import itemgetter
from multiprocessing import Pool
from time import time
from parser import parse_arguments



def spin_times(spins: int) -> tuple[int, int]:
    """
    Simulate a single round with N spins, and determine the longest sequence for both outcomes

    :param spins: The number of spins (coin flips) per round
    :return: Longest sequence of 1s, longest sequence of 0s
    """
    results: list[bool] = [random() >= 0.5 for _ in range(spins)]
    max_reds: list[int] = []
    max_blacks: list[int] = []
    for value, sequence in groupby(results):
        if value:
            max_reds.append(sum(sequence))
        else:
            max_blacks.append(len(list(sequence)) - sum(sequence))
    return max(max_reds), max(max_blacks)


def run_batch(rounds: int=100, spins_per_round: int=100, threads: int=1) -> tuple[int, int]:
    """
    Run many rounds concurrently with separate threads (GIL-indipendent)

    :param rounds: Number of simulations (rounds) to run
    :param spins_per_round: The number of spins (coin flips) per round
    :param threads: Number of threads to spawn for the simulation
    :return: The longest sequence of 1s and 0s from all simulations
    """
    with Pool(threads) as pool:
        results: list[tuple[int, int]] = pool.map(spin_times, [spins_per_round]*rounds, chunksize=100000)
    longest_red_sequence: int = max(results, key=itemgetter(0))[0]
    longest_black_sequence: int = max(results, key=itemgetter(1))[1]
    return longest_red_sequence, longest_black_sequence


def main(args) -> None:
    """
    Main function which runs the simulation using the provided arguments

    :param args: The parsed arguments
    :return: None
    """
    rounds: int = args.rounds
    spins_per_round: int = args.spins
    threads: int = args.threads
    output_file: str = args.out

    t_start = time()
    result: tuple[int, int] = run_batch(rounds=rounds, spins_per_round=spins_per_round, threads=threads)
    t_end = time()
    text: str = f"--- SIMULATION ENDED ---\n" \
                f"Rounds: {rounds}\n" \
                f"Spins per round: {spins_per_round}\n" \
                f"\n" \
                f"Longest run of 'reds'/'heads': {result[0]}\n" \
                f"Longest run of 'blacks'/'tails': {result[1]}\n" \
                f"Total time of simulation: {round(t_end-t_start, 1)}s\n"
    print(text)
    if not output_file: return
    with open(output_file, "w", encoding="utf-8") as outfile:
        if outfile.writable():
            outfile.write(text)


if __name__ == '__main__':
    args = parse_arguments()
    main(args)
