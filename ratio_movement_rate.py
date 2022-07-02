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
    0.2493765586,
    0.2857142857,
    0,
    0.5,
    0.54,
    0.3822393822,
    0.1836065574,
    0.1585714286,
    0.1391625616,
    0.1021825397,
    0.08709677419,
    0.07014028056,
    0.09642857143,
    0.06382978723,
    0.04816513761,
    0.04684684685,
    0.02448579824,
    0.09725685786,
    0.0882852292,
    0.1479289941,
    0.1012216405,
    0.1431818182,
    0.1025641026,
    0.1327345309,
    0.1476238625,
    0.1622807018,
    0.1722488038,
    0.2095709571,
    0.1746216531,
    0.1477079796,
]

x_label = 'water/sand'
y_label = 'movement rate'

x_unit = 'g/g'
y_unit = 'cm/s'

title = f'{y_label} vs {x_label}'

uncertainty_types = {
    'constant': 0,
    'percentage': 1
}
uncertainty_type = uncertainty_types['constant']

uncertainty_x = 0.002
uncertainty_y = 0.01

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
