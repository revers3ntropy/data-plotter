PROJECT_ROOT = '/home/joseph/Projects/data-plotter/'

x_label = 'strain'
y_label = 'stress'

x_unit = 'm/m'
y_unit = 'Nm^-2'

title = f'{y_label} vs {x_label}'

uncertainty_types = {
    'constant': 0,
    'percentage': 1
}
uncertainty_type = uncertainty_types['percentage']

uncertainty_x = 0.1
uncertainty_y = 0.1

sig_figs = 2

min_grad = [5.2e+10, -2.2e7]
max_grad = [1e+11, -8e7]

colours = {
    'lobf': 'black',
    'min': 'red',
    'max': 'blue',
    'min-bounds': 'green',
    'max-bounds': 'green',
}

show_bounds = False
