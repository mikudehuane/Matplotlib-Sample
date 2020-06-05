import sys
import os.path as osp
from csv_pic import *

output_file = '.'.join([osp.split(sys.argv[0])[-1].split('.')[0], 'pdf'])

run_list = ['FedLaAvg-FCA', 'FedLaAvg-E5', 'FedLaAvg-ICA', 'FedLaAvg-E15']

max_it = 50000

legend_list = [f'{alg} (E=1)', f'{alg} (E=5)', f'{alg} (E=10)', f'{alg} (E=15)']

# color_list = ['blue', 'green', 'orange', 'red']
color_list = ['blue', 'green', 'orange', 'red']

# line_list = ['-'] * 4
line_list = [':', '--', '-', '-.']

plot_every_list = [1] * 4

# axin = [.65, .5, .2, .12]
axin = None
font = 30

xlim = [49000, 49950]
# xticks = [49000, 50000]
xticks = []
ylim = [57, 64]
# yticks = [58, 61, 64]
yticks = []

plot(run_list, legend_list, color_list, line_list, plot_every_list, output_file, max_it, font,
    axin, xlim, ylim, xticks, yticks, False)