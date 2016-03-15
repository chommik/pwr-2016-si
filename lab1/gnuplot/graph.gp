#load "gnuplot/unset-layout.gp"
#load "gnuplot/defaults.gp"
#load "gnuplot/layout-default.gp"

set datafile separator ":"

set term qt size 1280,400

plot "stats.dat" using 1:2 title 'min fitness' with lines, \
      "stats.dat" using 1:3 title 'max fitness' with lines, \
      "stats.dat" using 1:4 title 'avg fitness' with lines
