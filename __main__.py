import matplotlib.pyplot as plt

from frequency_rate_down import *


def sci_not(s):
    return ('{:.' + str(sig_figs) + 'e}').format(s)


def str_polynomial(coefficients):
    return ' '.join(
        f'{"{:3e}".format(co)}x^{len(coefficients) - i - 1}'
        for i, co in enumerate(coefficients)
    )


def format_uncertainty(u, unit='', type=uncertainty_type):
    if type == uncertainty_types['percentage']:
        return f'±{round(u * 100, sig_figs)}%'
    return f'±{round(u, sig_figs)} {unit}'


def clean_data(x, y):
    grads = [(x[i] / y[i]) for i in range(len(x))]
    diff = np.ma.array(grads).anom()

    x_ = []
    y_ = []

    anoms = []

    for i in range(len(x)):
        if diff[i] > anomaly_boundary or diff[i] < -anomaly_boundary:
            anoms.append(i)
            continue
        x_.append(x[i])
        y_.append(y[i])

    print(f'{len(x) - len(x_)} anomalies ({round((len(x) - len(x_)) / len(x) * 100, 2)}%) found {anoms}')

    return np.array(x_), np.array(y_)


def load_data_from_file():
    """
        Loads data from local files data_x.txt and data_y.txt
    :return: (x: list, y: list)
    """
    with open(PROJECT_ROOT + 'data_x.txt') as raw_x:
        with open(PROJECT_ROOT + 'data_y.txt') as raw_y:
            x = np.array(list(map(float, raw_x.read().split('\n'))))
            y = np.array(list(map(float, raw_y.read().split('\n'))))
            return clean_data(np.fromiter(map(code_x, x), float),
                              np.fromiter(map(code_y, y), float))


def get_data_from_config():
    print(data_x[0])
    return clean_data(
        np.fromiter(map(code_x, np.array(data_x)), float),
        np.fromiter(map(code_y, np.array(data_y)), float)
    )


def find_bounds(x, y):
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


def plot(x, y, max_bounds, min_bounds, gradient, uncertainty):
    """
        Plots all data
    :param uncertainty:
    :param x: x values
    :param y: y values
    :param max_bounds: (max gradient, max gradient x values, max gradient y values)
    :param min_bounds: (min gradient, min gradient x values, min gradient y values)
    :param gradient: string describing the gradient in scientific notation
    """
    # plot scatter of points

    plt.plot(x, y, 'o', color=colours['points'])
    # add error bars to all points
    if uncertainty_type == uncertainty_types['percentage']:
        plt.errorbar(x, y, y * uncertainty_y, x * uncertainty_x, barsabove='False', capsize=2, ls='none')
    else:
        plt.errorbar(x, y, uncertainty_x, uncertainty_y, barsabove='False', capsize=2, ls='none')

    # plot line of best fit
    g = np.polyfit(x, y, 1)
    if show_lobf:
        line, = plt.plot(np.unique(x), np.poly1d(g)(np.unique(x)))
        line.set_color(colours['lobf'])

    if show_max_min_grad:
        line, = plt.plot(np.unique(x), np.poly1d(max_grad)(np.unique(x)))
        line.set_color(colours['max'])
        line, = plt.plot(np.unique(x), np.poly1d(min_grad)(np.unique(x)))
        line.set_color(colours['min'])

    # plot the min and max bounds
    if show_bounds:
        line, = plt.plot(np.unique(max_bounds[1]), np.poly1d(max_bounds[0])(np.unique(max_bounds[1])))
        line.set_color(colours['max-bounds'])
        line, = plt.plot(np.unique(min_bounds[1]), np.poly1d(min_bounds[0])(np.unique(min_bounds[1])))
        line.set_color(colours['min-bounds'])

    # get the uncertainty and units and stuff
    grad_uncertainty = uncertainty_x + uncertainty_y
    grad_unit = f'{y_unit}/{x_unit}'
    if len(y_unit) > 2 or len(x_unit) > 2:
        grad_unit = f'({y_unit})/({x_unit})'

    if y_unit == x_unit:
        grad_unit = ''

    final_title = f'{title}'
    if show_gradient_in_title:
        final_title += f'\n {gradient} {grad_unit}'
        # final_title += f'{format_uncertainty(grad_uncertainty, grad_unit)}'
        final_title += f' (actual {format_uncertainty(uncertainty, grad_unit, uncertainty_types["constant"])}'
        final_title += f', {format_uncertainty(uncertainty / g[0], grad_unit, uncertainty_types["percentage"])})'
        final_title += f'\n Min: {sci_not(min_grad[0])} {grad_unit}, Max: {sci_not(max_grad[0])} {grad_unit}'

    # add labels to the graph
    # swap x and y values - why ??
    plt.xlabel(f'{x_label} ({x_unit}) {format_uncertainty(uncertainty_y, x_unit)}')
    plt.ylabel(f'{y_label} ({y_unit}) {format_uncertainty(uncertainty_x, y_unit)}')
    plt.title(final_title, {
        'fontsize': 'medium'
    })

    if show_fill:
        if uncertainty_type == uncertainty_types['percentage']:
            plt.fill_between(
                np.unique(x),
                np.poly1d(max_grad)(np.unique(x)),
                np.poly1d(min_grad)(np.unique(x)),
                alpha=0.2,
                interpolate=True
            )
        else:
            plt.fill_between(x, y - uncertainty, y + uncertainty_y, alpha=0.5)

    plt.show()


def main():
    if use_data_from_file:
        x, y = load_data_from_file()
    else:
        x, y = get_data_from_config()

    bounds_x, bounds_y = find_bounds(x, y)

    g = np.polyfit(x, y, 1)
    str_grad = sci_not(g[0])

    uncertainty = math.fabs(round((min_grad[0] - max_grad[0]) / 2, sig_figs))

    print('Eq:  ' + str_polynomial(g))
    print('Gradient:  ' + str_grad)
    print('Uncertainty: ' + str(round(uncertainty * 100, 2)) + '%')
    print(f'Min/Max Gradient: {sci_not(min_grad[0])} / {sci_not(max_grad[0])}')

    print(x[0])
    plot(x, y, bounds_x, bounds_y, str_grad, uncertainty)


if __name__ == '__main__':
    main()
