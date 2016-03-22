# -*- coding: utf-8 -*-
import logging
import os
import random

from typing import TypeVar, List, io

import numpy

MODE_GREATER = 1
MODE_LOWER = 2

T = TypeVar("T")


class Problem:
    def initialise(self, population_size: int) -> List[T]:
        raise NotImplementedError

    def select_item(self, population: List[T]) -> T:
        raise NotImplementedError

    def fitness_for(self, item: T) -> int:
        raise NotImplementedError

    def crossover(self, item1: T, item2: T) -> T:
        raise NotImplementedError

    def mutate(self, item: T, mutation_chance: float) -> T:
        raise NotImplementedError

    def increment_step(self) -> int:
        raise NotImplementedError

    def should_stop(self, population) -> bool:
        raise NotImplementedError

    def get_stats(self) -> list:
        raise NotImplementedError


class GeneticAlgorithm:
    def __init__(self, problem: Problem, population_size: int, max_iterations: int, crossover_chance: float,
                 mutation_chance: float, graph_output: io, stats_output: io):
        self.stats_output = stats_output
        self.graph_output = graph_output
        self.mutation_chance = mutation_chance
        self.crossover_chance = crossover_chance
        self.max_iterations = max_iterations
        self.problem = problem
        self.population_size = population_size
        self.generation = 1
        self.population = []

    def show_stats(self):
        max_fitness, min_fitness, total_fitness = self.get_fitness_stats()

        logging.info("Generation %d/%d: Fitness: min = %d,\t max = %d,\t avg = %f,\t std = %f",
                     self.generation, self.max_iterations,
                     min_fitness, max_fitness, total_fitness / len(self.population), numpy.std(self.population))

        print("%d:%d:%d:%f" % (self.generation, min_fitness, max_fitness, total_fitness / len(self.population)), file=self.graph_output)

    def print_overall_stats(self, output=None):
        max_fitness, min_fitness, total_fitness = self.get_fitness_stats()
        avg_fitness = total_fitness / len(self.population)

        problem_stats = self.problem.get_stats()
        algo_stats = [
            self.max_iterations,
            len(self.population),
            max_fitness,
            avg_fitness,
            os.getpid(),
        ]

        if output is None:
            output = self.stats_output

        print(':'.join(str(item) for item in problem_stats + algo_stats), file=output)

    def get_fitness_stats(self):
        total_fitness = 0
        max_fitness = None
        min_fitness = None
        for item in self.population:
            fitness = self.problem.fitness_for(item)

            total_fitness += fitness
            if min_fitness is None or fitness < min_fitness:
                min_fitness = fitness
            if max_fitness is None or fitness > max_fitness:
                max_fitness = fitness
        return max_fitness, min_fitness, total_fitness

    def lets_rumble(self):
        logging.info("Let's rumble!")

        self.population = self.problem.initialise(self.population_size)

        while not (self.problem.should_stop(self.population) or self.generation >= self.max_iterations):
            self.generation = self.problem.increment_step()

            new_population = list()
            while len(new_population) < self.population_size:

                # Crossover?
                if random.random() < self.crossover_chance:
                    # Yes.
                    item1 = self.problem.select_item(self.population)
                    item2 = self.problem.select_item(self.population)
                    new_item = self.problem.crossover(item1, item2)
                else:
                    # Nope.
                    new_item = self.problem.select_item(self.population)

                new_item = self.problem.mutate(new_item, self.mutation_chance)

                new_population.append(new_item)

            self.population = new_population
            self.show_stats()

        self.print_overall_stats()

        if not self.problem.should_stop(self.population):
            logging.warning("Did not found a good solution.")
            return 1

        return 0
