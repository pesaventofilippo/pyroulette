''' PyRoulette - parser.py '''
import argparse



def parse_arguments():
    '''Funzione base del parser'''
    parser = argparse.ArgumentParser(
        prog="pyroulette.py",
        description=("Simulate a coin flip and determine the longest sequence of 1s and 0s"),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-r',
        '--rounds',
        type=int,
        default=100,
        help='Number of simulations (rounds) to run'
    )
    parser.add_argument(
        '-s',
        '--spins',
        '--spins-per-round',
        type=int,
        default=100,
        help='The number of spins (coin flips) per round'
    )
    parser.add_argument(
        '-t',
        '--threads',
        '--cpu',
        type=int,
        default=1,
        help='Number of threads to spawn for the simulation'
    )
    parser.add_argument(
        '-o',
        '--out',
        type=str,
        default=None,
        help='File to save the results'
    )
    return parser.parse_args()
