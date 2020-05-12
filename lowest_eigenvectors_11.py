from numpy import loadtxt, linalg, asarray

# written by E.Hansen
# write try:/except: OSError for filename when importing module

data = loadtxt(input('Input Matrix File: '), dtype='i')  # import the data
array = asarray(data)   # convert data to array
(w, v) = linalg.eig(array)    # find eigenvalues/eigenvectors; w is eigenvalue, v is eigenvector
w.sort()    # change eigenvalues to ascending order

