# -*- coding: utf-8 -*-
import logging
import random

from typing import TypeVar, List

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

    def mutate(self, item: T) -> T:
        raise NotImplementedError

    def increment_step(self) -> int:
        raise NotImplementedError

    def should_stop(self) -> bool:
        raise NotImplementedError


class GeneticAlgorithm:
    def __init__(self, problem: Problem, population_size: int, max_iterations: int, crossover_chance: float,
                 mutation_chance: float):
        self.mutation_chance = mutation_chance
        self.crossover_chance = crossover_chance
        self.max_iterations = max_iterations
        self.problem = problem
        self.population_size = population_size
        self.generation = 1
        self.population = []

    def show_stats(self):
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

        logging.info("Generation %d/%d: Fitness: min = %d,\t max = %d,\t avg = %f",
                     self.generation, self.max_iterations,
                     min_fitness, max_fitness, total_fitness / len(self.population))

    def lets_rumble(self):
        logging.info("Let's rumble!")

        self.population = self.problem.initialise(self.population_size)

        while not (self.problem.should_stop() or self.generation >= self.max_iterations):
            self.generation = self.problem.increment_step()

            new_population = []
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

                # Mutate?
                if random.random() < self.mutation_chance:
                    new_item = self.problem.mutate(new_item)

                new_population.append(new_item)

            self.population = new_population
            self.show_stats()

