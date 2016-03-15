# -*- coding: utf-8 -*-
import argparse
import logging
import sys
import genetic_algo
import graph_problem


def setup_logging():
    log_format = "{asctime} {levelname:8} {threadName:<15} [{module}:{lineno}] {message}"
    logging.basicConfig(format=log_format, style="{", level=logging.DEBUG)

def get_parameters():
    parser = argparse.ArgumentParser('genes.py')

    parser.add_argument('--max-colours', type=int, required=True)
    parser.add_argument('--graph-file', type=str, required=True)
    parser.add_argument('--iterations', type=int, required=True)
    parser.add_argument('--population-size', type=int, required=True)

    parser.add_argument('--crossover-chance', type=float, required=True)
    parser.add_argument('--mutation-chance', type=float, required=False)

    return parser.parse_args()

def main():
    setup_logging()
    params = get_parameters()

    graph_problem.load_graph("graphs/GEOM20.col", params.max_colours)
    stats_output = open('stats.dat', 'w+')

    algo = genetic_algo.GeneticAlgorithm(graph_problem.GraphProblem(), params.population_size, params.iterations,
                                         params.crossover_chance, params.mutation_chance, stats_output)
    exit_code = algo.lets_rumble()
    stats_output.close()

    sys.exit(exit_code)

if __name__ == "__main__":
    main()