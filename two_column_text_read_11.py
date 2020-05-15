from numpy import *

# written by E.Hansen

# create list from text data and assign variables to columns


def two_column_text_read(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))

        return x, y


try:

    (x, y) = two_column_text_read('Pb.Fm-3m.GGA-PBE.volumes_energies.dat.txt')  # input filename
    x1 = array(x)
    y1 = array(y)  # turn list variables into array
    read_data = column_stack((x1, y1))  # group data into x, y points

except OSError:
    print('Filename cannot be found')   # error checking
