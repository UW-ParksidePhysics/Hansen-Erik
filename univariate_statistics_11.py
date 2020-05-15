from numpy import *
from Final_exam.two_column_text_read_11 import x1, y1

# written by E.Hansen
# write try:/except ImportError statement when importing module


def univariate_statistics():

    """outputs the statistics into an array"""

    if len(x1) >= 3:  # check for length of list
        if len(y1) >= 1:    # check for a y-value column
            if len(x1) == len(y1):  # verify arrays have equal length
                my_names = ('StdDev(Y):', 'Mean(Y):', 'X-min:', 'X-max:', 'Y-min', 'Y-max')  # label printed stats
                my_stats1 = (std(y1), mean(y1), min(x1), max(x1), min(y1), max(y1))  # define stats
                return column_stack((my_names, my_stats1))  # group labels with defined stats
    else:
        print('IndexError: Data has inappropriate dimensions')  # error checking



