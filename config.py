import math
import numpy as np

PROJECT_ROOT = '/Users/josephcoppin/PycharmProjects/graphplotting/'

x_label = 'sin(θ1)'
y_label = 'sin(θ2)'

x_unit = '°'
y_unit = '°'

title = f'{y_label} vs {x_label}'

uncertainty_types = {
    'constant': 0,
    'percentage': 1
}
uncertainty_type = uncertainty_types['constant']

uncertainty_x = 0.05
uncertainty_y = 0.05

sig_figs = 2

min_grad = [1.1, 0.15]
max_grad = [1.8, -0.1]

colours = {
    'lobf': 'black',
    'points': 'black',
    'min': 'red',
    'max': 'blue',
    'min-bounds': 'green',
    'max-bounds': 'green',
}

show_bounds = 0
show_max_min_grad = 1
show_fill = 0
show_lobf = 1


def code_x(x):
    return np.sin(x / (180/math.pi))


def code_y(y):
    return np.sin(y / (180/math.pi))
