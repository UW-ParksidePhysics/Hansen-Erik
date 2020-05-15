from numpy import *
from Final_exam.quadratic_fit_11 import quadratic_fit, x1

# written by E.Hansen

x = linspace(float(min(x1)), float(max(x1)))    # defining the x-range of the array
fit_curve = polyval(quadratic_fit(), x)    # generating the fit curve
array_data = column_stack((x, fit_curve))   # grouping the x, y coordinates
