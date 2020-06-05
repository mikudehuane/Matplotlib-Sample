import csv
from matplotlib import pyplot as plt
import os.path as osp
import numpy as np
from copy import deepcopy

alg = 'FedLaAvg'
def plot(run_list, legend_list, color_list, line_list, plot_every_list, output_file, max_it=1000000, font=15,
    axin=None, xlim=None, ylim=None, xticks=None, yticks=None, reverse=False, filt=None, loc=None,
    x_tick_interval=10000, alpha_list=None, legend_order=None):

    num_lines = len(legend_list)

    if alpha_list is None:
        alpha_list = [1] * num_lines
    if filt is None:
        filt = list(range(num_lines))
    if legend_order is None:
        legend_order = deepcopy(filt)

    run_list = np.array(run_list)[filt].tolist()
    legend_list = np.array(legend_list)[filt].tolist()
    color_list = np.array(color_list)[filt].tolist()
    line_list = np.array(line_list)[filt].tolist()
    plot_every_list = np.array(plot_every_list)[filt].tolist()

    filt_inverse = [-1] * len(filt)
    for i, idx in enumerate(filt):
        filt_inverse[idx] = i
    
    lines = [None] * len(legend_list)

    if reverse:
        run_list = run_list[::-1]
        legend_list = legend_list[::-1]
        color_list = color_list[::-1]
        line_list = line_list[::-1]
        plot_every_list = plot_every_list[::-1]

    filep_list = [osp.join('data', run + '.csv') for run in run_list]
    steps_list = []
    values_list = []

    for filep, plot_every in zip(filep_list, plot_every_list):
        with open(filep) as f:  
            reader = csv.reader(f)
            next(reader)
            steps = [int(row[1]) for row in reader]
        with open(filep) as f:
            reader = csv.reader(f)
            next(reader)
            values = [float(row[2]) * 100 for row in reader]
        low = 0
        proc_steps = []
        proc_values = []
        for step, value in zip(steps, values):
            if max_it >= step >= low:
                proc_steps.append(step)
                proc_values.append(value)
                low += plot_every
            else:
                continue
        steps_list.append(proc_steps)
        values_list.append(proc_values)

    fig = plt.figure(dpi=128, figsize=(10, 6))

    for line_idx, (steps, values, color, line, alpha, label) in enumerate(zip(steps_list, values_list, color_list, line_list, alpha_list, legend_list)):
        lines[line_idx], = plt.plot(steps, values, line, c=color, linewidth=1.0, alpha=alpha, label=label)

    font1 = {
        'family' : 'Times New Roman',
        'size'   : font,
    }
    
    plt.xlabel('Communication Rounds', fontdict=font1)
    plt.ylabel('Test Accuracy (%)', fontdict=font1)
    ticks_x = [str(num//1000) for num in range(0, max_it + 50, x_tick_interval)]
    plt.xticks(list(range(0, max_it + 50, x_tick_interval)), ticks_x, fontsize=font, fontfamily='Times New Roman')
    plt.yticks(fontsize=font, fontfamily='Times New Roman')

    handles = np.array(lines)[filt_inverse][legend_order].tolist()
    plt.legend(handles=handles, prop=font1, frameon=False, labelspacing=0.4, loc=loc)

    import matplotlib as mpl

    ticklabelpad = mpl.rcParams['xtick.major.pad']
    plt.annotate('10$^\mathregular{3}$', xy=(1,0), ha='left', va='top',
            xycoords='axes fraction', textcoords='offset points', fontfamily='Times New Roman', fontsize=font)

    if axin is not None:
        a = plt.axes(axin)
        for steps, values, color, line in zip(steps_list, values_list, color_list, line_list):
            plt.plot(steps, values, line, c=color, linewidth=3.0)
        plt.xlim(*xlim)
        plt.ylim(*ylim)
        plt.xticks(xticks, [str(x // 1000) for x in xticks], size=font, family='Times New Roman')
        plt.yticks(yticks, size=font, family='Times New Roman')
        plt.annotate('10$^\mathregular{3}$', xy=(1,0), ha='left', va='top',
                xycoords='axes fraction', textcoords='offset points', fontfamily='Times New Roman', fontsize=font)

    plt.tight_layout()
    plt.savefig(osp.join('fig', output_file))
    plt.show()