import sys
import os.path as osp
from csv_pic import *

import csv
import os.path as osp

"""
:plot_order: define the order to plot lines 
:legend_order: define the order to put legends, by defaut same with plot_order

:legend_loc: location to put the legends
:fraemon: whether to add fraemon to legends
:label_spacing: label_spacing for legends

:x_ticks: tuple of steps and text
:x_annotation: annotation at the end of x_ticks, e.g. 10^3
"""

output_fn = '.'.join([osp.split(sys.argv[0])[-1].split('.')[0], 'pdf'])
output_fp = osp.join('fig', output_fn)

run_list = ['SGD', 'FedLaAvg-ICA', 'FedLaAvg-FCA', 'FedAvg-ICA', 'FedAvg-FCA', 'FedLaAvg-outlier']

x_label = 'Communication Rounds'
y_label = 'Test Accuracy (%)'

legend_list = ['Sequential SGD', f'{alg} (ICA)', f'{alg} (FCA)',
    'FedAvg (ICA)', 'FedAvg (FCA)', 'FedLaAvg (ICA with Outliers)']
color_list = ['red', 'orange', 'blue', 'green', 'purple', 'black']
alpha_list = [1, 1, 1, 1, 1, 1]   # transparent degree
line_list = ['--', '-', '-', ':', ':', '-']
plot_every_list = [1, 1, 1, 1, 1, 100]
line_width_list = [1, 1, 1, 1, 1, 1]

max_it = 70000
min_it = 5000

font = 21

subfigure_pars = dict(
    axin=[.7, .35, .2, .3],
    xlim=[69000, 70100],
    xticks=([69000, 70000], [69, 70]),
    ylim=[53, 65],
    yticks=[54, 57, 60, 63],
    line_width=3.0,
    x_annotation='$10^3$'
)

plot_order = [2, 1, 4, 3]
legend_order=[2, 1, 4, 3]

legend_loc = ("lower right", (0.65, 0.1))
fraemon = False
label_spacing = 0.4

x_tick_interval = 10000
x_ticks_step = list(range(min_it, max_it + 1, x_tick_interval))
x_ticks_text = ['$' + str(num//1000) + '$' for num in x_ticks_step]
x_ticks = x_ticks_step, x_ticks_text

y_ticks = (range(30, 61, 10),) * 2

x_annotation = "$10^3$"

y_scaling = 100

plot(
    run_list=run_list, output_fp=output_fp,
    x_label=x_label, y_label=y_label,
    legend_list=legend_list, color_list=color_list, line_list=line_list,
    plot_every_list=plot_every_list, alpha_list=alpha_list, line_width_list=line_width_list,
    max_it=max_it, min_it=min_it, font=font,
    subfigure_pars=subfigure_pars,
    plot_order=plot_order, legend_order=legend_order, 
    legend_loc=legend_loc, fraemon=fraemon, label_spacing=label_spacing,
    x_ticks=x_ticks, x_annotation=x_annotation, y_ticks=y_ticks,
    y_scaling=y_scaling
)