# pyroulette
A Python script to simulate sequences of roulette spins (or coin flips).


## Why?
This project was inspired by [UpAndAtom's video](https://www.youtube.com/watch?v=XA_0OMJjkxQ) about the Gambler's Fallacy.  
After hearing that one time Monte Carlo's Casino rolled 26 blacks in a row in the roulette game (a 1 in 66 million chance), I wanted to figure out what was the (reasonable) limit of such an occurrence.


## What does this do?
The `main.py` script simulates N rounds of X spins each.  
For example, with N=10 and X=100, the scripts simulates 10 games of roulette, where in every round the roulette gets spun 100 times. The scripts then prints the length of the longest sequences of reds (heads) and blacks (tails) respectively. (see [CLI Arguments](#Arguments))


## Usage
To run the script, just start it with `python3 main.py`.  
If you want, there are additional arguments to modify the simulation parameters.


### Arguments
- `-r N`, `--rounds N`: The number of simulations (rounds) to run (default: 100)  
- `-s N`, `--spins N`, `--spins-per-round N`: The number of spins (coin flips) per round (default: 100)  
- `-t N`, `--threads N`: The number of threads to spawn for the simulation (default: 1, doesn't multithread)  
- `-o filename`, `--out filename`: Optional file name to write the simulation results after it ended. The program also always prints the results to stdout, so if the parameter isn't specified or the file isn't writable, you can see the results.  

You can provide these arguments in no particular order, or omit some or all of them.


## Optimization
This code is optimized only to a certain extent (being written in python doesn't help).
If you want to improve the main function (spin_times()), you can use the `bench.py` file: you must write a function (your_algorithm()) that, when called, generates 100 random outcomes (1 or 0) and returns the logest sequences for both outcomes.  
When you finished writing, you can test it against the original algorithm by running `python3 bench.py`, which will run both functions 5 times and determine the best one (by execution time).  
If your function is faster than mine and produces the same output, feel free to create a pull request!
