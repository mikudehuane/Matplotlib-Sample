# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 3:13 下午
# @Author  : islander
# @File    : preprocess.py
# @Software: PyCharm

"""define the common preprocesses for data

functions defined returns a preprocess function that transform data in the defined way
"""
import bisect
from typing import Callable
from typing import List, Tuple


FUNCTION_PROTOCOL = Callable[[List, List], Tuple[List, List]]


def get_sample_data_at_equal_x_interval(interval) -> FUNCTION_PROTOCOL:
    """sample data such that the interval between the x coordinates of two dots on the graph is no less than interval

    Args:
        interval: minimum interval between the x coordinates of two dots
    """
    def func(x_values, y_values):
        low = 0
        new_x_values = []
        new_y_values = []
        for x_val, y_val in zip(x_values, y_values):
            if x_val >= low:
                new_x_values.append(x_val)
                new_y_values.append(y_val)
                low += interval
            else:
                continue
        return new_x_values, new_y_values

    return func


def get_scale_y(scale) -> FUNCTION_PROTOCOL:
    """scale y values by scale

    Args:
        scale: multiply each y element by scale
    """
    def func(x_values, y_values):
        y_values = [val * scale for val in y_values]
        return x_values, y_values

    return func


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
