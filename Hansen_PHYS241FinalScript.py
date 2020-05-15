from Final_exam.two_column_text_read_11 import x1, y1
from Final_exam.quadratic_fit_11 import quadratic_fit
from Final_exam.univariate_statistics_11 import univariate_statistics
from Final_exam.fit_curve_array_11 import x
import Final_exam.plot_data_with_fit_11
import matplotlib.pyplot as plt
from Final_exam.equations_of_state import fit_eos
from numpy import *

"""Read in the data into a NumPy array using your two_column_text_read function"""
"""Pull out the statistics on the data set using your univariate_statistics function """
"""Fit a quadratic polynomial to the data using your quadratic_fit function """


def parse_file_name():      # part 1
    file_name = 'Pb.Fm-3m.GGA-PBE.volumes_energies.dat.txt'
    symbol = file_name.split('.')[0]
    symmetry = file_name.split('.')[1]
    density = file_name.split('.')[2]
    return symbol, symmetry, density


""" Extract the chemical symbol, crystal symmetry symbol, density functional exchange-correlation
approximation acronym from your give data file's name"""

print('Stats:', univariate_statistics())  # pulling out the stats, part 3

"""Pull out the statistics on the data set using your univariate_statistics function from the Final Review;"""

quadratic_fit()

"""Fit a quadratic polynomial to the data using your quadratic_fit function from the Final Review"""

fit_eos(x1, y1, quadratic_fit(), eos='vinet')

"""Pass the fit quadratic coefficients and the data to the fit_eos function linked through the
Final Exam Data page, passing the parameters assigned to you"""


"""def convert_units(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            x.append(1.48185e-61 * float(line[0]))  # bohr^3 to angstrom^3
            y.append(13.6056980659 * float(line[1]))  # rydberg to ev
            return x, y


(x, y) = convert_units('Pb.Fm-3m.GGA-PBE.volumes_energies.dat.txt')"""

"""Convert that data and fit from atomic units,
 to these units using a module you write called convert_units:"""


"""plt.plot(fit_eos)"""
plt.xlim([min(x1) * .9, max(x1) * 1.1])     # generating a plot based off volume_energies data given
plt.ylabel('E(eV/atom)')
plt.xlabel('V(Å3/atom)')

"""Plot the data and the fit function with volume on the horizontal axis and 
energy on the vertical axis:"""


def annotate_graph():
    plt.text(90, -11844.40922, 'Pb')
    plt.text(111, -11844.50922, 'Fm-3m')
    plt.text(111, -11844.48922, 'GGA-PBE')
    plt.axvline(x=100, ymin=-11844.51765, ymax=-11844.4, color='k', label='equillibium volume')
    plt.text(87, -11844.525, 'Created by Erik Hansen 2020-05-12')
    return


"""Write a function called annotate_graph"""


annotate_graph()

display_graph = 'tru'
if display_graph == 'true':
    plt.show()
else:
    plt.savefig('Hansen.Pb.Fm-3m.GGA-PBE.VinetEquationOfState.png')

"""Finally, declare (in the parameters section of the script) a variable called display_graph, 
which is a Boolean value that calls PyPlot's show function when True, and savefig when False"""


"""This wasn't my best attempt at the code, but I decided to submit what worked and created a graph.
I struggled getting all the data through the convert and equation of state without getting an error"""

