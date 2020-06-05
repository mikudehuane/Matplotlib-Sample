import sys
import os.path as osp
from csv_pic import *

import csv
import os.path as osp

output_file = '.'.join([osp.split(sys.argv[0])[-1].split('.')[0], 'pdf'])

run_list = ['FedLaAvg-ICA', 'multistep', 'FedAvg-ICA']

legend_list = [f'{alg} (exp)', f'{alg} (multistep)', 'FedAvg (exp)']

color_list = ['orange', 'blue', 'green']

line_list = ['-', '-', ':']

plot_every_list = [1] * 3

max_it = 25000

axin = [.7, .45, .2, .3]
font = 21

xlim = [69000, 70100]
xticks = [69000, 70000]
ylim = [53, 65]
yticks = [54, 57, 60, 63]

plot(run_list, legend_list, color_list, line_list, plot_every_list, output_file, max_it, font,
    axin=[0,0,0,0], xlim=[0, 0], ylim=[0,0], xticks=[], yticks=[], filt=[0, 1, 2], loc=4, x_tick_interval=5000)