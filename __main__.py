import math
import matplotlib.pyplot as plt
import numpy as np


PROJECT_ROOT = '/Users/josephcoppin/PycharmProjects/graphplotting/'


def str_polynomial(coefficients):
    return ' '.join(
        f'{"{:e}".format(co)}x^{len(coefficients) - i - 1}'
        for i, co in enumerate(coefficients)
    )


with open(PROJECT_ROOT + 'data_x.txt') as data_x:
    with open(PROJECT_ROOT + 'data_y.txt') as data_y:
        x = np.array(list(map(lambda d: float(d), data_x.read().split('\n'))))
        y = np.array(list(map(lambda d: float(d), data_y.read().split('\n'))))

x_label = input('X label: ') or 'x'
y_label = input('Y label: ') or 'y'
title = input('Title: ') or 'title'

uncertainty_type = int(input('Uncertainty type (0=constant, 1=%)') or 1)

uncertainty_x = float(input('Uncertainty X: ') or 0.1)
uncertainty_y = float(input('Uncertainty Y: ') or 0.1)

# plotting the points
plt.scatter(x, y)
if uncertainty_type == 1:
    plt.errorbar(x, y, x * uncertainty_x / 100., y * uncertainty_y / 100., barsabove='False')
else:
    plt.errorbar(x, y, uncertainty_x, uncertainty_y)


max_x = uncertainty_x + x
min_x = uncertainty_x - x
max_y = uncertainty_x + y
min_y = uncertainty_x - y

if uncertainty_type == 1:
    max_x = np.fromiter((n + n * uncertainty_x for n in x), float)
    min_x = np.fromiter((n - n * uncertainty_x for n in x), float)

    max_y = np.fromiter((n + n * uncertainty_x for n in y), float)
    min_y = np.fromiter((n - n * uncertainty_x for n in y), float)

# plot max and mins
if uncertainty_x != 0 or uncertainty_y != 0:
    plt.scatter(max_x, max_y)
    plt.scatter(min_x, min_y)
    plt.scatter(max_x, min_y)
    plt.scatter(min_x, max_y)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

gradients = [
    (np.polyfit(x, y, 1), x, y),
    (np.polyfit(min_x, y, 1), min_x, y),
    (np.polyfit(max_x, y, 1), x, y),
    (np.polyfit(x, min_y, 1), x, y),
    (np.polyfit(min_x, min_y, 1), x, y),
    (np.polyfit(max_x, min_y, 1), x, y),
    (np.polyfit(x, max_y, 1), x, y),
    (np.polyfit(min_x, max_y, 1), x, y),
    (np.polyfit(max_x, max_y, 1), x, y)
]
print('Eq:  ' + str_polynomial(np.polyfit(x, y, 1)))
print('Gradient:  ' + '{:e}'.format(np.polyfit(x, y, 1)[0]))

min_g = ([math.inf], )
max_g = ([-math.inf], )
for g in gradients:
    if g[0][0] < min_g[0][0]:
        min_g = g

    if g[0][0] > max_g[0][0]:
        max_g = g

print('Max gradient: ' + '{:e}'.format(max_g[0][0]))
print('Min gradient: ' + '{:e}'.format(min_g[0][0]))

plt.plot(np.unique(max_x), np.poly1d(np.polyfit(max_x, max_y, 1))(np.unique(max_x)))
plt.plot(np.unique(min_x), np.poly1d(np.polyfit(min_x, min_y, 1))(np.unique(min_x)))

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.show()
