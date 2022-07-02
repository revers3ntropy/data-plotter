import math
import numpy as np

PROJECT_ROOT = ''

use_data_from_file = False

data_y = [
    0.02037037037,
    0.002777777778,
    0.02808641975,
    0.200308642,
    0.6313131313,
    0.01481481481,
    0.09444444444,
    0.1688888889,
    0.5694444444,
    0,
    0.05709876543,
    0.6972222222,
    0,
    0.3127340824,
    0.6541005291,
    0.2614197531,
    0.5921985816,
    0.3089506173,
    0.5208333333,
    0,
    0,
    0.03073286052,
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

uncertainty_x = 0.1
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
