# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 3:50 下午
# @Author  : islander
# @File    : __init__.py
# @Software: PyCharm

from .plot import plot as plot  # v1 plot

from .plot_v2 import plot as plot2
from .plot_v2 import get_font

from . import preprocess

import matplotlib as mpl

# set math and ordinary fonts to be consistent
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
