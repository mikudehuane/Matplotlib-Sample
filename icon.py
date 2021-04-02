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

output_fn = '.'.join((osp.split(sys.argv[0])[-1]).split('.')[:-1] + ['pdf'])
output_fp = osp.join('fig', output_fn)

run_list = ['test_400000']

x_label = u'Iteration'
y_label = u'Test AUC'

legend_list = None
color_list = None
alpha_list = None
line_list = None
plot_every_list = None
line_width_list = None

max_it = 1000
min_it = 0

font = 21

subfigure_pars = None

plot_order = None
legend_order = None

legend_loc = ("lower right", (0.65, 0.1))
fraemon = False
label_spacing = 0.4

x_ticks = None

y_ticks = None

x_annotation = None

y_scaling = 1

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
    y_scaling=y_scaling, x_column=0, y_column=2, chinese_font=True,
)