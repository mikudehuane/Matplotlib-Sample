import sys
import os.path as osp
from csv_pic import *
import numpy as np

output_file = '.'.join((osp.split(sys.argv[0])[-1]).split('.')[:-1] + ['pdf'])

run_list = ['FedLaAvg-N200', 'FedLaAvg-N400', 'FedLaAvg-N600', 'FedLaAvg-N800', 'FedLaAvg-ICA']

legend_list = [f'{alg} ($N=200$)', f'{alg} ($N=400$)', f'{alg} ($N=600$)', f'{alg} ($N=800$)', f'{alg} ($N=1000$)']

# color_list = ['purple', 'blue', 'green', 'red', 'orange']
color_list = ['red', '-', 'blue', '-', 'orange']

# line_list = ['-'] * 5
line_list = [':', '-', '--', '-', '-']

plot_every_list = [1] * 5

filt = [0, 2, 4]

max_it = 50000

# axin = [.65, .55, .2, .12]
axin = None
font = 30

xlim = [49000, 49950]
# xticks = [49000, 50000]
xticks = []
ylim = [53, 63]
# yticks = [54, 58, 62]
yticks = []

reverse = True

plot(run_list, legend_list, color_list, line_list, plot_every_list, output_file, max_it, font,
    axin, xlim, ylim, xticks, yticks, reverse, filt)