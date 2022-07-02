import math
import numpy as np

PROJECT_ROOT = ''

use_data_from_file = False

data_y = [
    0.0003254360844,
    0.0001561996779,
    0.003933747412,
    0.0006570048309,
    0.0002499484642,
    0.000266028199,
    0.002063299885,
    0.002758888032,
    0.009647473561,
    0.009617266074,
    0.01142709696,
    0.0134795274,
    0.01216291643,
    0.01004347826,
    0.009643576859,
    0.009797966965,
    0.008192176351,
    0.001709486166,
    0.01295311279,
    0.01494098312,
    0.01439850598,
    0.0197160721,
    0.01959281029,
    0.01647194024,
    0.01348153549,
    0.01315285753,
    0.01646027031,
    0.0002481365047,
    0.002501484382,
    0.007029105837,
]
data_x = [
    5.01,
    4.5,
    5.04,
    0.75,
    3.08,
    3.58,
    7.22,
    8.11,
    9.25,
    11.11,
    13.48,
    16.02,
    6.14,
    7.5,
    9.14,
    5.81,
    10.46,
    4.4,
    6.41,
    5.82,
    6.31,
    5.03,
    5.59,
    11.35,
    11.35,
    10.6,
    7.35,
    7.33,
    10.09,
    6.76
]

x_label = 'mass'
y_label = 'movement rate'

x_unit = 'g'
y_unit = 'cm/s'

title = f'{y_label} vs {x_label}'

uncertainty_types = {
    'constant': 0,
    'percentage': 1
}
uncertainty_type = uncertainty_types['constant']

uncertainty_x = 0.003
uncertainty_y = 2

sig_figs = 2

min_grad = [5*10**-4, 0]
max_grad = [2*10**-3, 0]

colours = {
    'lobf': 'black',
    'points': 'black',
    'min': 'red',
    'max': 'blue',
    'min-bounds': 'green',
    'max-bounds': 'green',
}

show_bounds = 0
show_max_min_grad = 0
show_fill = 0
show_lobf = 1
show_gradient_in_title = 1


def code_x(x):
    return x


def code_y(y):
    return y


anomaly_boundary = 10000000
