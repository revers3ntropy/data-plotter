import math
import numpy as np

PROJECT_ROOT = ''

use_data_from_file = False

data_y = [
    0,
    0.05925925926,
    0,
    0,
    0,
    0,
    8.578431373,
    11.2,
    16.37037037,
    0.2751817238,
    0.3037037037,
    0,
    0,
    0,
    0.007936507937,
    0,
    0,
    0,
    0,
    1.418518519,
    7.933333333
]
data_x = [
    100,
    90,
    80,
    70,
    60,
    110,
    50,
    40,
    30,
    200,
    300,
    400,
    500,
    450,
    350,
    320,
    400,
    380,
    360,
    250,
    50
]

x_label = 'frequency'
y_label = 'movement rate'

x_unit = 'Hz'
y_unit = 'g/cm/s'

title = f'{y_label} vs {x_label}'

uncertainty_types = {
    'constant': 0,
    'percentage': 1
}
uncertainty_type = uncertainty_types['constant']

uncertainty_x = 1.6
uncertainty_y = 7

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
show_lobf = 0
show_gradient_in_title = 0


def code_x(x):
    return x


def code_y(y):
    return y


# very large for no anomaly detection
anomaly_boundary = 10**100
