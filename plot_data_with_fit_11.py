import matplotlib.pyplot as plt
from Final_exam.fit_curve_array_11 import x, fit_curve
import numpy as np
from Final_exam.two_column_text_read_11 import x1, y1

# written by E.Hansen

plt.plot(x, fit_curve, color='k', label='Curve Fit')  # plotting the array data
plt.scatter(x1, y1, label='Data Points')
plt.legend()
