#!/bin/bash

GRAPH="graphs/GEOM20.col"
COL_MIN=20
COL_MAX=23
ITERATIONS=1000

for popsize in 100
do
    for generations in 1000
    do
        for try in {0..10}
        do
            echo python3.5 genes.py \
                --graph-file $GRAPH \
                --max-colours 22 \
                --iterations $generations \
                --population-size $popsize \
                --crossover-chance 0.85 \
                --mutation-chance 0.015 \
                \&\>/dev/null
        done
    done
done
