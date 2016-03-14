# -*- coding: utf-8 -*-
import logging
from math import sqrt
import random

from typing import List
import numpy
import scipy.stats
from genetic_algo import Problem

colours_count = -1
vertex_count = -1
edges = []

generation = 0


def load_graph(file_name: str, _max_colours: int) -> None:
    global vertex_count, colours_count

    colours_count = _max_colours

    logging.info("Loading graph from '%s'", file_name)
    with open(file_name) as input_file:
        for line in input_file:
            tokens = line.strip().split()

            if tokens[0] == "c":  # comment
                pass
            elif tokens[0] == "p":  # problem: "p some_junk total_vertices total_edges"
                vertex_count = int(tokens[3])
            elif tokens[0] == "e":  # edge: "e from_vert to_vert min_distance"
                edges.append((int(tokens[1]) - 1, int(tokens[2]) - 1, int(tokens[3])))
            elif tokens[0] == "n":  # vertex: "vertex number some_junk"
                pass

    logging.info("vertex_count: %d, max_colours: %d, edges: %r", vertex_count, colours_count, edges)


class GraphItem(object):
    colouring = []
    unfitness = None

    def __getitem__(self, item):
        return self.colouring[item]

    def __setitem__(self, key, value):
        self.colouring[key] = value

    def __len__(self):
        return len(self.colouring)

    def __init__(self, colouring):
        self.colouring = tuple(colouring)


def random_colouring() -> GraphItem:
    return GraphItem(
        [random.randrange(1, colours_count + 1) for _ in range(vertex_count)]
    )


class GraphProblem(Problem):
    def crossover(self, item1: GraphItem, item2: GraphItem) -> GraphItem:
        crossover_point = random.randrange(0, len(item1))
        # FIXME: brzydkie
        return GraphItem(
            item1.colouring[:crossover_point] + item2.colouring[crossover_point:]
        )

    def should_stop(self, population) -> bool:
        return any(self.fitness_for(item) == 0 for item in population)

    def mutate(self, item: GraphItem) -> GraphItem:
        which_vertex = random.randrange(0, len(item))
        new_value = random.randrange(0, colours_count + 1)

        new_colouring = list(item.colouring)
        new_colouring[which_vertex] = new_value

        return GraphItem(new_colouring)

    def select_item(self, population: List[GraphItem]) -> GraphItem:
        some_items = [random.choice(population) for _ in range(10)]
        return max(some_items, key=lambda item: self.fitness_for(item))

    def increment_step(self) -> int:
        global generation
        generation += 1

        return generation

    def initialise(self, population_size: int) -> List[GraphItem]:
        logging.info("creating population of size %d", population_size)
        return list(random_colouring() for _ in range(population_size))

    def fitness_for(self, item: GraphItem) -> int:
        if item.unfitness is None:
            unfitness = 0

            for edge in edges:
                from_vert, to_vert, min_distance = edge
                vert1_colour, vert2_colour = item[from_vert], item[to_vert]

                colour_distance = abs(vert1_colour - vert2_colour)
                if colour_distance < min_distance:
                    unfitness -= colour_distance

            item.unfitness = unfitness
        else:
            unfitness = item.unfitness

        return unfitness