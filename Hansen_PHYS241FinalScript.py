from Final_exam.two_column_text_read_11 import read_data, x1, y1
from Final_exam.quadratic_fit_11 import quadratic_fit
from Final_exam.univariate_statistics_11 import univariate_statistics
import matplotlib.pyplot as plt
from Final_exam.fit_curve_array_11 import array_data, fit_curve, x
import Final_exam.plot_data_with_fit_11
from Final_exam.equations_of_state import fit_eos
import numpy as np

"""Read in the data into a NumPy array using your two_column_text_read function"""
"""Pull out the statistics on the data set using your univariate_statistics function """
"""Fit a quadratic polynomial to the data using your quadratic_fit function """


def parse_file_name():
    return print('Pb, Fm-3m, GGA-PBE')


""" Extract the chemical symbol, crystal symmetry symbol, density functional exchange-correlation
approximation acronym from your give data file's name"""

"""def convert_units():
    x2 = 1.48185e-61 * x  # bohr^3 to angstrom^3
    y2 = 13.6056980659 * y  # rydberg to ev
    z2 = y2/x2
    return x2, y2, z2

COULDN'T FIGURE OUT HOW TO CONVERT PROPERLY SO I DID IT OUTSIDE OF PYTHON"""

print('Stats:', univariate_statistics())  # printing the stats
fit_eos(y1, x1, quadratic_fit(), eos='vinet')
plt.xlim([min(x1) * .9, max(x1) * 1.1])
plt.xlabel('E(eV/atom)')
plt.ylabel('V(Å3/atom)')
plt.plot(fit_eos)
plt.show()

