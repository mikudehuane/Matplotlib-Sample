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
        input_fps, output_fp='figure/raw.png',
        data_format_config=data_format_config
    )
    plt.show()


if __name__ == '__main__':
    main()
