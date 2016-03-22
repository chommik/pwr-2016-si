#load "gnuplot/unset-layout.gp"
#load "gnuplot/defaults.gp"
#load "gnuplot/layout-default.gp"

set datafile separator ":"

set term png size 1280,600

plot "graph.dat" using 1:2 title 'min fitness' with lines, \
      "graph.dat" using 1:3 title 'max fitness' with lines, \
      "graph.dat" using 1:4 title 'avg fitness' with lines
