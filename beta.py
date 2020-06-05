import sys
import os.path as osp
from csv_pic import *

output_file = '.'.join([osp.split(sys.argv[0])[-1].split('.')[0], 'pdf'])

run_list = ['FedLaAvg-beta0.02', 'FedLaAvg-beta0.04', 'FedLaAvg-beta0.06', 'FedLaAvg-beta0.08', 'FedLaAvg-ICA']

max_it = 50000

legend_list = [f'{alg} (β=0.02)', f'{alg} (β=0.04)', f'{alg} (β=0.06)', f'{alg} (β=0.08)', f'{alg} (β=0.10)']

# color_list = ['purple', 'blue', 'green', 'red', 'orange']
color_list = ['red', '-', 'blue', '-', 'orange']

filt = [0, 2, 4]

line_list = ['--', '-', ':', None, '-']

plot_every_list = [1] * 5

reverse = True

# axin = [.7, .55, .15, .12]
axin = None
font = 30

xlim = [49000, 49950]
# xticks = [49000, 50000]
xticks = []
ylim = [55, 62]
# yticks = [56, 59, 62]
yticks = []

plot(run_list, legend_list, color_list, line_list, plot_every_list, output_file, max_it, font,
    axin, xlim, ylim, xticks, yticks, reverse, filt)