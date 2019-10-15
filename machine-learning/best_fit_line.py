from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def best_fit_slope_intercept(x, y):
    slope = (((mean(x) * mean(y)) - mean(x * y)) /
             ((mean(x) * mean(x)) - mean(x * x)))
    intercept = mean(y) - slope * mean(x)
    return slope, intercept


def squared_error(ys_orig, ys_line):
    return sum((ys_orig - ys_line) ** 2)


def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_reg = squared_error(ys_orig, ys_line)
    squared_error_yhat = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_reg/squared_error_yhat)


m, b = best_fit_slope_intercept(xs, ys)
regression_line = [m*x+b for x in xs]
print(m, b, regression_line)

predict_x = 8
predict_y = (m*predict_x)+b
print(predict_y)

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)