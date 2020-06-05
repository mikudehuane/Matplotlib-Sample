import sys
import os.path as osp
from csv_pic import *

import csv
import os.path as osp

output_file = '.'.join([osp.split(sys.argv[0])[-1].split('.')[0], 'pdf'])

run_list = ['SGD', 'FedLaAvg-ICA', 'FedLaAvg-FCA', 'FedAvg-ICA', 'FedAvg-FCA', 'FedLaAvg-outlier']

legend_list = ['Sequential SGD', f'{alg} (ICA)', f'{alg} (FCA)',
    'FedAvg (ICA)', 'FedAvg (FCA)', 'FedLaAvg (ICA with outliers)']

# color_list = ['red', 'orange', 'blue', 'green', 'purple']
color_list = ['red', 'orange', 'blue', 'green', 'purple', 'black']

alpha_list = [1, 1, 1, 1, 1, 1]   # transparent degree

line_list = ['--', '-', '-', ':', ':', '-']

plot_every_list = [1, 1, 1, 1, 1, 100]

max_it = 70000

axin = [.7, .45, .2, .3]
font = 21

xlim = [69000, 70100]
xticks = [69000, 70000]
ylim = [53, 65]
yticks = [54, 57, 60, 63]

plot(run_list, legend_list, color_list, line_list, plot_every_list, output_file, max_it, font,
    axin, xlim, ylim, xticks, yticks, filt=[0, 2, 5, 1, 4, 3], loc=8, alpha_list=alpha_list,
    legend_order=[0, 2, 1, 4, 3, 5])