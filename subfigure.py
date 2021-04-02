# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 5:45 下午
# @Author  : islander
# @File    : raw.py
# @Software: PyCharm


import csv_pic
import os.path as osp
from matplotlib import pyplot as plt


def main():
    input_fps = [osp.join('data', fn) for fn in ['0.csv', '1.csv', '2.csv', '3.csv']]

    data_format_config = {
        'x': 1,
        'y': 2,
    }

    csv_pic.plot2(
        input_fps,
        preprocesses=[csv_pic.preprocess.get_streamed_preprocess([
            csv_pic.preprocess.get_sample_data_at_equal_x_interval(1000),
            csv_pic.preprocess.get_scale_y(100),
        ])] * 4,
        data_format_config=data_format_config,
        x_label_config={'text': 'step'}, y_label_config={'text': 'accuracy (%)'},
        legend_config={'text': [r'$\beta$=0.1', r'$\beta$=0.2', r'$\beta$=0.3', '中文\n$\\beta$=0.4'],
                       'loc': ('lower left', (0, 1.02, 1, 0.2)),  'labelspacing': 1.0,
                       'font_dict': csv_pic.get_font('song.ttf', 25),
                       'order': (3, 0, 2, 1),
                       'ncol': 4, 'borderaxespad': 0, 'mode': 'expand', 'frameon': True},
        line_configs=[
            {'color': 'red', 'line': ':', 'alpha': 0.3, 'width': 5},
            {'color': 'blue', 'line': '-.', 'alpha': 0.9, 'width': 1},
            {'color': 'orange', 'line': '-', 'width': 1},
            {'color': 'grey', 'line': '--', 'alpha': 1.0, 'width': 1},
        ],
        plot_order=[2, 1, 0, 3],
        x_tick_config={'ticks': [0, 10000, 20000, 30000, 40000],
                       'labels': [0, 10, 20, 30, 40],
                       'lim': [0, 45000]},
        x_annotation_config={'text': '10^3'}
    )
    # noinspection PyTypeChecker
    plt.axes((.7, .2, .2, .3))  # [left, bottom, width, height] for the subplot
    csv_pic.plot2(
        input_fps,
        preprocesses=[csv_pic.preprocess.get_streamed_preprocess([
            csv_pic.preprocess.get_sample_data_at_equal_x_interval(1000),
            csv_pic.preprocess.get_scale_y(100),
        ])] * 4,
        figure_config='inherit',
        data_format_config=data_format_config,
        legend_config=None,
        line_configs=[
            {'color': 'red', 'line': ':', 'alpha': 0.3, 'width': 5},
            {'color': 'blue', 'line': '-.', 'alpha': 0.9, 'width': 1},
            {'color': 'orange', 'line': '-', 'width': 1},
            {'color': 'grey', 'line': '--', 'alpha': 1.0, 'width': 1},
        ],
        plot_order=[2, 1, 0, 3],
        x_tick_config={'ticks': [39000, 40000],
                       'labels': [39, 40],
                       'lim': [39000, 40100]},
        y_tick_config={'ticks': [50, 60],
                       'labels': [50, 60],
                       'lim': [50, 60]},
        x_annotation_config={'text': '10^3'}
    )
    plt.savefig('figure/subfigure.png')
    plt.show()


if __name__ == '__main__':
    main()
