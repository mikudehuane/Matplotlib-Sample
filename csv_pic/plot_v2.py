import csv
from typing import List, Dict, Callable, Tuple, Union

import matplotlib as mpl
from matplotlib import pyplot as plt
import os.path as osp
import numpy as np
from copy import deepcopy

from . import preprocess
from . import default_config
from . import utils


def get_font(font_fn, font_size):
    """construct the font from an external font file and a given size

    Args:
        font_fn: file name of the font, put in font/
        font_size: size of the required font
    """
    # noinspection PyUnresolvedReferences
    ret = mpl.font_manager.FontProperties(fname=osp.join('font', font_fn))
    ret.set_size(font_size)
    return ret


def plot(
        input_fps: List[str], output_fp: str = None, *,
        preprocesses: List[Callable[[List, List], Tuple[List, List]]] = None,
        data_format_config: Dict = None,
        figure_config: Dict = None,
        x_label_config: Dict = None, y_label_config: Dict = None,
        legend_config: Dict = None,
        line_configs: List[Dict] = None,
        plot_order: List[int] = None,
        x_tick_config: Dict = None, y_tick_config: Dict = None,
        x_annotation_config: Dict = None,
) -> None:
    """plot a figure from csv data (2-dim lines)

    Args:
        input_fps: path to each input data files
        output_fp: path to the output figure file, if None, do not output

        preprocesses: list of preprocesses of input data, same order with input_fps
            preprocess(x_values, y_values) -> (new_x_values, new_y_values)
        data_format_config: config for the data format, by default {'x': 0, 'y': 1}
            'x': column number of x axis
            'y': column number of y axis
        figure_config: config for the figure, by default {'size': (10, 6), 'dpi': 128}
            'size': size of the output figure, given as (width, height)
            'dpi': precision of the output figure
        x_label_config: config for x label, by default None (no label)
            'text': label text
            'font_dict': font given as a dict
                'size': font size
        y_label_config: config for y label, by default None (no label)
            format same as x_label_config
        legend_config: config for legend, by default None (no legend)
            'text': list of texts for each legend, same order with input_fps
            'loc': location for legend
            'frameon': whether legend has frame
            'order': order of the legends on the graph, given as a list of <index in input_fps>
                None by default, means use the natural order
            'label_spacing': vertical space between two labels
            'font_dict': font given as a dict
        line_configs: list of configs for each line, same order with input_fps,
            each config with the following format, None means use pyplot default
                'color': given as 'red', 'blue', etc.
                'line': line style, given as '-', ':', '.-', etc.
                'alpha': transparent level, given as float value in [0, 1], 1 means opaque
                'width': line width, given as float value, 1 by default
        plot_order: order to plot the lines on the graph, given as a list of <index in input_fps>
        x_tick_config: config for x ticks
            'ticks': tick locations (coordinate on the graph)
            'labels': texts to be ticks on the axis
            'fontsize': size of the tick font
            'lim': axis range (only show data that are within the range in the plot),
                None means follow matplotlib default
        y_tick_config: config for y ticks, same format with x_tick_config
        x_annotation_config: config for the annotation on x axis
            'text': annotated text
            'xy': coordinate for the annotation
            'fontsize': size of the annotation font

    Notes:
        - configures, if given and not complete, will load default values of not given keys from .default_config
        - not given keys in configures (after filled with default) are all filled with None
    """
    num_lines = len(input_fps)

    if preprocesses is None:
        preprocesses = [None] * num_lines
    if line_configs is None:
        line_configs = [None] * num_lines

    # get config, if None, return default, else update default by the given config
    def _get_config(_config: Union[Dict, None], _default_config: Dict):
        _ret = deepcopy(_default_config)
        if _config is not None:
            _ret.update(_config)
        return _ret

    # get config, if None, return None, else update  default by the given config
    def _get_config_reserve_none(_config: Union[Dict, None], _default_config: Dict):
        if _config is None:
            return None
        else:
            _ret = deepcopy(_default_config)
            _ret.update(_config)
            return _ret

    data_format_config = _get_config(data_format_config, default_config.DATA_FORMAT_CONFIG)
    figure_config = _get_config(figure_config, default_config.FIGURE_CONFIG)

    x_label_config = _get_config_reserve_none(x_label_config, default_config.X_LABEL_CONFIG)
    y_label_config = _get_config_reserve_none(y_label_config, default_config.Y_LABEL_CONFIG)

    legend_config = _get_config_reserve_none(legend_config, default_config.LEGEND_CONFIG)

    line_configs = [_get_config(config, default_config.LINE_CONFIG) for config in line_configs]

    if plot_order is None:
        plot_order = list(range(num_lines))

    x_tick_config = _get_config_reserve_none(x_tick_config, default_config.X_TICK_CONFIG)
    y_tick_config = _get_config_reserve_none(y_tick_config, default_config.Y_TICK_CONFIG)

    x_annotation_config = _get_config_reserve_none(x_annotation_config, default_config.X_ANNOTATION_CONFIG)

    # get the data to be plotted
    data_values = [utils.get_data(fp, config=data_format_config, preprocess=proc)
                   for fp, proc in zip(input_fps, preprocesses)]

    fig = plt.figure(dpi=figure_config['dpi'], figsize=figure_config['size'])

    if legend_config is None:
        legend_texts = [None] * num_lines
    else:
        legend_texts = legend_config['text']
    lines = [None] * num_lines
    for line_idx in plot_order:
        x_values, y_values = data_values[line_idx]
        config = line_configs[line_idx]
        lines[line_idx] = utils.plot_line(x_values, y_values, config=config, label=legend_texts[line_idx])

    utils.legend(lines, config=legend_config)

    if x_tick_config is not None:
        utils.tick(loc='x', config=x_tick_config)
    if y_tick_config is not None:
        utils.tick(loc='y', config=y_tick_config)

    if x_label_config is not None:
        plt.xlabel(x_label_config['text'], fontdict=x_label_config['font_dict'])
    if y_label_config is not None:
        plt.ylabel(y_label_config['text'], fontdict=y_label_config['font_dict'])

    if x_annotation_config is not None:
        plt.annotate(x_annotation_config['text'], xy=x_annotation_config['xy'],
                     ha='left', va='top', xycoords='axes fraction', textcoords='offset points',
                     fontsize=x_annotation_config['fontsize'])

    plt.tight_layout()

    if output_fp is not None:
        plt.savefig(output_fp)
