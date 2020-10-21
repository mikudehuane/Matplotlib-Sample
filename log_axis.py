import sys
import os.path as osp
from plot_sample.csv_pic import *

import csv
import os.path as osp

import math

"""
:plot_order: define the order to plot lines 
:legend_order: define the order to put legends, by defaut same with plot_order

:legend_loc: location to put the legends
:fraemon: whether to add fraemon to legends
:label_spacing: label_spacing for legends

:x_ticks: tuple of steps and text
:x_annotation: annotation at the end of x_ticks, e.g. 10^3
"""

output_fn = '.'.join((osp.split(sys.argv[0])[-1]).split('.')[:-1] + ['pdf'])
output_fp = osp.join('fig', output_fn)

run_list = ['mFedAvg/train_loss', 'FedLaAvg/train_loss']

x_label = 'Communication Rounds'
y_label = 'Training loss'

legend_list = ['momentum FedAvg', 'FedLaAvg']
color_list = ['red', 'blue']
alpha_list = [1, 1]
line_list = ['-', '-']
plot_every_list = [1, 1]
line_width_list = [1, 1]

max_it = 70000
min_it = 0

font = 21

# subfigure_pars = dict(
#     axin=[.68, .45, .2, .3],
#     xlim=[69000, 70100],
#     xticks=([69000, 70000], [69, 70]),
#     ylim=[53, 62],
#     yticks=[54, 57, 60],
#     line_width=3.0,
#     x_annotation='$10^3$'
# )
subfigure_pars = None

plot_order = None
legend_order = None

legend_loc = ("upper right", (0.95, 0.95))
fraemon = False
label_spacing = 0.4

x_tick_interval = 10000
x_ticks_step = list(range(min_it, max_it + 1, x_tick_interval))
x_ticks_text = ['$' + str(num//1000) + '$' for num in x_ticks_step]
x_ticks = x_ticks_step, x_ticks_text

y_ticks_tick = ['1', '3', '7', '20']
y_ticks_value = [math.log(float(y)) for y in y_ticks_tick]
y_ticks = (y_ticks_value, y_ticks_tick)

x_annotation = "$10^3$"

y_scaling = 1.0

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
    y_scaling=y_scaling, chinese_font=False, log_axis=True
)