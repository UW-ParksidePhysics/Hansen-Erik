from numpy import polyfit
from Final_exam.two_column_text_read_11 import x1, y1

# written by E.Hansen


def quadratic_fit():
    """imports array data and outputs the 2nd order quadratic equation"""

    if len(x1) >= 3:  # check for length of list
        if len(y1) >= 1:    # check for a y-value column
            if len(x1) == len(y1):  # verify arrays have equal length
                return polyfit(x1, y1, 2)   # create a second order quadratic equation

        else:
            print('IndexError: Data has inappropriate dimensions')

