set term png size 1280,600

# file : max_colouts : failed_constraints : max_generations : last_generation : max_fitness : avg_fitness : crossover_chance : mutation_chance : PID
#    1       2               3                   4               5               6               7               8                   9               10

set datafile separator whitespace
plot "stats-processed2.dat" using 1:2:3 with image
