import math
import matplotlib.pyplot as plt
import numpy as np

from config import *


def sci_not(s):
    return ('{:.' + str(sig_figs) + 'e}').format(s)


def str_polynomial(coefficients):
    return ' '.join(
        f'{"{:3e}".format(co)}x^{len(coefficients) - i - 1}'
        for i, co in enumerate(coefficients)
    )


def format_uncertainty(u, unit=''):
    if uncertainty_type == uncertainty_types['percentage']:
        return f'±{u * 100}%'
    return f'±{u} {unit}'


def load_data():
    """
        Loads data from local files data_x.txt and data_y.txt
    :return: (x: list, y: list)
    """
    with open(PROJECT_ROOT + 'data_x.txt') as data_x:
        with open(PROJECT_ROOT + 'data_y.txt') as data_y:
            x = np.array(list(map(lambda d: float(d), data_x.read().split('\n'))))
            y = np.array(list(map(lambda d: float(d), data_y.read().split('\n'))))

            return x, y


def find_min_max(x, y):
    max_x = uncertainty_x + x
    min_x = uncertainty_x - x
    max_y = uncertainty_x + y
    min_y = uncertainty_x - y

    if uncertainty_type == 1:
        max_x = np.fromiter((n + n * uncertainty_x for n in x), float)
        min_x = np.fromiter((n - n * uncertainty_x for n in x), float)

        max_y = np.fromiter((n + n * uncertainty_x for n in y), float)
        min_y = np.fromiter((n - n * uncertainty_x for n in y), float)

    possibilities = [
        (min_x, y),
        (max_x, y),
        (x, min_y),
        (min_x, min_y),
        (max_x, min_y),
        (x, max_y),
        (min_x, max_y),
        (max_x, max_y)
    ]

    min_g = ([math.inf],)
    max_g = ([-math.inf],)
    for x_set, y_set in possibilities:
        g = np.polyfit(x_set, y_set, 1)
        if g[0] < min_g[0][0]:
            min_g = (g, x_set, y_set)

        if g[0] > max_g[0][0]:
            max_g = (g, x_set, y_set)

    return min_g, max_g


def plot(x, y, max_g, min_g, gradient):
    """
        Plots all data
    :param x: x values
    :param y: y values
    :param max_g: (max gradient, max gradient x values, max gradient y values)
    :param min_g: (min gradient, min gradient x values, min gradient y values)
    :param gradient: string describing the gradient in scientific notation
    """
    plt.scatter(x, y)
    if uncertainty_type == 1:
        plt.errorbar(x, y, y * uncertainty_y, x * uncertainty_x, barsabove='False')
    else:
        plt.errorbar(x, y, uncertainty_x, uncertainty_y)

    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

    plt.plot(np.unique(max_g[1]), np.poly1d(max_g[0])(np.unique(max_g[1])))
    plt.plot(np.unique(min_g[1]), np.poly1d(min_g[0])(np.unique(min_g[1])))

    grad_uncertainty = uncertainty_x + uncertainty_y
    grad_unit = f'{y_unit}/{x_unit}'

    plt.xlabel(f'{x_label} ({x_unit}) {format_uncertainty(uncertainty_x, x_unit)}')
    plt.ylabel(f'{y_label} ({y_unit}) {format_uncertainty(uncertainty_y, y_unit)}')
    plt.title(f'{title} - {gradient} {grad_unit} {format_uncertainty(grad_uncertainty, x_unit)}')
    plt.show()


def main():
    x, y = load_data()

    min_g, max_g = find_min_max(x, y)

    str_grad = sci_not(np.polyfit(x, y, 1)[0])

    print('Eq:  ' + str_polynomial(np.polyfit(x, y, 1)))
    print('Gradient:  ' + str_grad)
    print('Max gradient: ' + sci_not(max_g[0][0]))
    print('Min gradient: ' + sci_not(min_g[0][0]))

    plot(x, y, max_g, min_g, str_grad)


if __name__ == '__main__':
    main()
