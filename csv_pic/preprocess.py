# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 3:13 下午
# @Author  : islander
# @File    : preprocess.py
# @Software: PyCharm

"""define the common preprocesses for data

functions defined returns a preprocess function that transform data in the defined way
"""

from typing import Callable
from typing import List, Tuple


FUNCTION_PROTOCOL = Callable[[List, List], Tuple[List, List]]


def get_sample_data_at_equal_x_interval(interval) -> FUNCTION_PROTOCOL:
    """sample data such that the interval between the x coordinates of two dots on the graph is no less than interval

    Args:
        interval: minimum interval between the x coordinates of two dots
    """
    # TODO(islander): finish function
    ...


def get_clamp_x_range(x_min=float('-inf'), x_max=float('inf')) -> FUNCTION_PROTOCOL:
    """clamp data to reserve only data whose x coordinate is within the range of [x_min, x_max]

    Args:
        x_min: minimum x value
        x_max: maximum x value
    """
    # TODO(islander): finish function
    ...


def get_scale_y(scale) -> FUNCTION_PROTOCOL:
    """scale y values by scale

    Args:
        scale: multiply each y element by scale
    """
    # TODO(islander): finish function
    ...


def get_streamed_preprocess(preprocesses: List[FUNCTION_PROTOCOL]) -> FUNCTION_PROTOCOL:
    """stream the preprocesses given as a new preprocess

    Args:
        preprocesses: list of used preprocesses, data will be transformed in the following way:
            data -preprocess[0]-> data -preprocess[1]-> data -...-> data
    """
    def func(x_values, y_values):
        for preprocess in preprocesses:
            x_values, y_values = preprocess(x_values, y_values)
        return x_values, y_values

    return func


def identity_map(x_values: List, y_values: List) -> Tuple[List, List]:
    return x_values, y_values
