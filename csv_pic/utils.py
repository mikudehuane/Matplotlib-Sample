# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 4:51 下午
# @Author  : islander
# @File    : utils.py
# @Software: PyCharm
from copy import deepcopy
from typing import Dict, List
import numpy as np
from matplotlib import pyplot as plt


def legend(handlers: List, config: Dict):
    config = deepcopy(config)
    # legend location
    legend_loc = config.pop('loc', None)
    legend_kwargs = {}
    if legend_loc is not None:
        legend_loc, legend_bbox = legend_loc
        legend_kwargs['bbox_to_anchor'] = legend_bbox
        legend_kwargs['loc'] = legend_loc

    # legend order
    legend_order = config.pop('order', None)
    if legend_order is None:
        legend_order = list(range(len(handlers)))
    handlers = [handlers[idx] for idx in legend_order]

    prop = config.pop('font_dict')

    config.pop('text', None)  # remove unused key

    plt.legend(fancybox=True, handles=handlers, prop=prop,
               **legend_kwargs, **config)


def tick(loc, config: Dict):
    lim = config.get('lim', None)
    lim_func = plt.xlim if loc == 'x' else plt.ylim
    if lim is not None:
        lim_func(*lim)

    ticks = config.get('ticks', None)
    tick_func = plt.xticks if loc == 'x' else plt.yticks
    if ticks is not None:
        tick_func(ticks=config['ticks'], labels=config['labels'], fontsize=config['fontsize'])


def plot_line(x_values, y_values, config, label=None):
    pars_dict = {}
    if config.get('color', None) is not None:
        pars_dict['c'] = config['color']
    if label is not None:
        pars_dict['label'] = label
    line = plt.plot(
        x_values, y_values,
        config['line'], linewidth=config['width'], alpha=config['alpha'],
        **pars_dict
    )
    return line[0]


def get_data(data_fp, config, preprocess=None, skip_heading=True):
    x_col = config['x']
    y_col = config['y']
    with open(data_fp) as f:
        if skip_heading:
            f.readline()
        content = f.readlines()
    # strip lines and split
    content = [line.strip().split(',') for line in content]
    content = [(line[x_col], line[y_col]) for line in content]
    content = np.array([(float(x), float(y)) for x, y in content])
    x_values = content[:, 0]
    y_values = content[:, 1]

    if preprocess is not None:
        x_values, y_values = preprocess(x_values, y_values)

    return x_values, y_values
