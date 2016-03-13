# -*- coding: utf-8 -*-

from typing import TypeVar, List


MODE_GREATER = 1
MODE_LOWER = 2

T = TypeVar("T")


class Problem:
    comparison_mode = MODE_LOWER

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

    def increment_step(self) -> None:
        raise NotImplementedError

    def should_stop(self) -> bool:
        raise NotImplementedError


class GeneticAlgorithm:
    def __init__(self, problem: Problem, population_size: int):
        self.problem = problem
        self.population = population_size



