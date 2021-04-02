# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 3:02 下午
# @Author  : islander
# @File    : default_config.py
# @Software: PyCharm

DATA_FORMAT_CONFIG = {
    'x': 0,
    'y': 1,
}

FIGURE_CONFIG = {
    'size': (10, 6),
    'dpi': 128,
}

X_LABEL_CONFIG = {
    'font_dict': {'size': 15}
}

Y_LABEL_CONFIG = {
    'font_dict': {'size': 15}
}

LEGEND_CONFIG = {
    'frameon': False,
    'labelspacing': 0.4,
    'font_dict': {'size': 15},
    'ncol': 1
}

LINE_CONFIG = {
    'line': '-',
    'alpha': 1,
    'width': 1,
}

X_TICK_CONFIG = {
    'fontsize': 15,
}

Y_TICK_CONFIG = {
    'fontsize': 15,
}

X_ANNOTATION_CONFIG = {
    'xy': (1, 0),
    'fontsize': 15
}
