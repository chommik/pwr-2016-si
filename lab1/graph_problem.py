# -*- coding: utf-8 -*-

from typing import io, List
from genetic_algo import Problem

graph = None
max_colours = -1
vertex_count = -1


def load_graph(file_name: str, _max_colours: int) -> None:
    max_colours = _max_colours

    with open(file_name) as input_file:
        for line in input_file:
            tokens = line.strip().split()


class GraphItem(object):
    colouring = []

    __getitem__ = colouring.__getitem__
    __setitem__ = colouring.__setitem__
    __iter__ = colouring.__iter__

    def __init__(self, colouring):
        self.colouring = colouring


def random_colouring() -> GraphItem:
    pass


class GraphProblem(Problem):
    def crossover(self, item1: GraphItem, item2: GraphItem) -> GraphItem:
        pass

    def should_stop(self) -> bool:
        pass

    def mutate(self, item: GraphItem) -> GraphItem:
        pass

    def select_item(self, population: List[GraphItem]) -> GraphItem:
        pass

    def increment_step(self) -> None:
        pass

    def initialise(self, population_size: int) -> List[GraphItem]:
        pass

    def fitness_for(self, item: GraphItem) -> int:
        pass

