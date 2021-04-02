import csv
import matplotlib as mpl
from matplotlib import pyplot as plt
import os.path as osp
import numpy as np
from copy import deepcopy
from matplotlib import rc
from matplotlib import font_manager as fm, rcParams

alg = 'FedLaAvg'


def plot(
        run_list, output_fp, x_column=1, y_column=2,
        fig_size=(10, 6),
        x_label=None, y_label=None,
        legend_list=None, color_list=None, line_list=None, plot_every_list=None, alpha_list=None, line_width_list=None,
        max_it=None, min_it=0, font=15,
        subfigure_pars=None,
        plot_order=None, legend_order=None,
        legend_loc=None, fraemon=True, label_spacing=0.4,
        x_ticks=None, x_annotation=None, y_ticks=None,
        main_graph_y_lim=None,
        y_scaling=1, chinese_font=False,
        log_axis=False
):
    """
    :run_list: list of csv file names (discarding '.csv'), or list of data (x, y)
    :output_fp: the output file name
    :x_column: data column for x
    :y_column: data column for y

    :x_label, y_label: labels

    :legend_list: list of legends to be added to the figure
    :color_list: list of line colors
    :line_list: list of line styles
    :plot_every_list: the minimum interval of points
    :alpha_list: list of transparent degress
    :line_width_list: list of line width

    :max_it: maximum number of iterations
    :font: font size for all text in the figure

    :subfigure_pars: if not None, plot a subfigure with pars 
        axin, xlim, yline, xticks (tuple), yticks (subfigure size, subfigure range, subfigure ticks)
        line_width array or scalar (by default 3.0)
        x_annotation
    
    :plot_order: define the order to plot lines 
    :legend_order: define the order to put legends, by defaut same with plot_order

    :legend_loc: location to put the legends loc / (loc, bbox_to_anchor)
        for example ("upper right", (0.5, 0.5)) put the upper right corner on (x=0.5, y=0.5)
    :fraemon: whether to add fraemon to legends
    :label_spacing: label_spacing for legends

    :x_ticks: tuple of steps and text
    :x_annotation: annotation at the end of x_ticks, e.g. 10^3

    :main_graph_y_lim: y axis limitation, (low, high)

    :y_scaling: scaling y axis ticks (y_ticks has higher priority)

    :log_axis: log scaling y axis, pass appropriate y_ticks to corporate,
        processed after y_scaling
    """

    # rc('text', usetex=True)
    # rc('font',**{'family':'serif','serif':['Times New Roman'],'weight':'roman'})

    # set math and ordinary fonts to be consistent
    mpl.rcParams['mathtext.fontset'] = 'stix'
    mpl.rcParams['font.family'] = 'STIXGeneral'

    num_lines = len(run_list)

    legend_loc_dict = {}
    if isinstance(legend_loc, tuple):
        legend_loc, legend_bbox = legend_loc
        legend_loc_dict['bbox_to_anchor'] = legend_bbox
    legend_loc_dict['loc'] = legend_loc

    if plot_every_list is None:
        plot_every_list = [1] * num_lines
    if legend_list is None:
        legend_list = [None] * num_lines
    if color_list is None:
        color_list = [None] * num_lines
    if line_list is None:
        line_list = ['-'] * num_lines
    if alpha_list is None:
        alpha_list = [1] * num_lines
    if line_width_list is None:
        line_width_list = [1.0] * num_lines

    if plot_order is None:
        plot_order = list(range(num_lines))
    if legend_order is None:
        legend_order = deepcopy(plot_order)

    if x_ticks is None:
        x_ticks = ()
    if y_ticks is None:
        y_ticks = ()

    lines = [None] * len(legend_list)

    steps_list = []
    values_list = []

    filep_list = [osp.join('data', run_name + '.csv') for run_name in run_list]

    for filep, plot_every in zip(filep_list, plot_every_list):
        with open(filep) as f:
            reader = csv.reader(f)
            next(reader)
            steps = [int(row[x_column]) for row in reader]
        with open(filep) as f:
            reader = csv.reader(f)
            next(reader)
            values = [float(row[y_column]) * y_scaling for row in reader]
        low = 0
        proc_steps = []
        proc_values = []
        for step, value in zip(steps, values):
            if (max_it is None or max_it >= step) and step >= min_it and step >= low:
                proc_steps.append(step)
                proc_values.append(value)
                low += plot_every
            else:
                continue
        steps_list.append(proc_steps)
        values_list.append(proc_values)

    fig = plt.figure(dpi=128, figsize=fig_size)

    plot_pars_array = list(
        zip(steps_list, values_list, color_list, line_list, alpha_list, legend_list, line_width_list))
    if main_graph_y_lim is not None:
        plt.ylim(*main_graph_y_lim)
    for line_idx in plot_order:
        steps, values, color, line, alpha, label, line_width = plot_pars_array[line_idx]
        if log_axis:
            values = np.log(values)
        pars_dict = {}
        if color is not None:
            pars_dict['c'] = color
        if label is not None:
            pars_dict['label'] = label
        lines[line_idx], = plt.plot(steps, values, line, linewidth=line_width, alpha=alpha,
                                    **pars_dict)

    font_dict = {
        'size': font,
    }

    if x_label is not None:
        plt.xlabel(x_label, fontdict=font_dict)
    if y_label is not None:
        plt.ylabel(y_label, fontdict=font_dict)

    plt.xticks(*x_ticks, fontsize=font)
    plt.yticks(*y_ticks, fontsize=font)

    handles = [None] * len(legend_order)
    for handles_idx, legend_idx in enumerate(legend_order):
        handle = lines[legend_idx]
        if handle is None:
            print(
                f"legend_order {legend_order} contradicts plot_order {plot_order}, since require legends on lines that are not plotted.")
            raise AssertionError()
        handles[handles_idx] = handle

    fontcn = mpl.font_manager.FontProperties(fname="song.ttf")
    fontcn.set_size(font)
    if chinese_font:
        legend_font = fontcn
    else:
        legend_font = font_dict
    fig.legend(fancybox=True, handles=handles, prop=legend_font, frameon=fraemon, labelspacing=label_spacing,
               **legend_loc_dict)

    if x_annotation is not None:
        plt.annotate(x_annotation, xy=(1, 0), ha='left', va='top', xycoords='axes fraction', textcoords='offset points',
                     fontsize=font)

    if subfigure_pars is not None:
        try:
            axin = subfigure_pars['axin']
            xlim, ylim = subfigure_pars['xlim'], subfigure_pars['ylim']
            xticks, yticks = subfigure_pars['xticks'], subfigure_pars['yticks']
        except KeyError as e:
            print("When plotting the subfigure, not enough parameters provided")
            raise e

        subfigure_line_width = subfigure_pars.get('line_width', 3.0)
        subfigure_x_annotation = subfigure_pars.get('x_annotation', None)

        if isinstance(subfigure_line_width, float):
            subfigure_line_width = [subfigure_line_width] * num_lines

        plt.axes(axin)
        _lines = [None] * len(legend_list)
        for line_idx in plot_order:
            steps, values, color, line, alpha, label, line_width = plot_pars_array[line_idx]
            pars_dict = {}
            if color is not None:
                pars_dict['c'] = color
            if label is not None:
                pars_dict['label'] = label
            _lines[line_idx], = plt.plot(steps, values, line, linewidth=3 * line_width, alpha=alpha, **pars_dict)
        plt.xlim(*xlim)
        plt.ylim(*ylim)
        plt.xticks(*xticks, size=font)
        plt.yticks(yticks, size=font)

        if subfigure_x_annotation is not None:
            plt.annotate(subfigure_x_annotation, xy=(1, 0), ha='left', va='top', xycoords='axes fraction',
                         textcoords='offset points', fontsize=font)

    fig.tight_layout()
    fig.savefig(output_fp)
    plt.show()
