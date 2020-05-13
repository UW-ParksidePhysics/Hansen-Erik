from Final_exam.generate_matrix import generate_matrix
from numpy import asarray, linalg, linspace
import matplotlib.pyplot as plt


x = generate_matrix(minimum_x=float(-10), maximum_x=float(10), number_of_dimensions=120, potential_name='sinusoidal',
                    potential_parameter=float(200))
array = asarray(x)   # convert data to array
(w, u) = linalg.eig(array)    # find eigenvalues/eigenvectors; w is eigenvalue, v is eigenvector
w.sort()   # change eigenvalues to ascending order
v = u[::-1]
n_dim = linspace(-10, 10, 120)
plt.plot(n_dim, u)
plt.axhline(y=0, color='k', label='Created by Erik Hansen 2020-05-12')
plt.xlabel('x[a.u.]')
plt.ylabel('y[a.u.]')
plt.ylim(-.5, .5)
plt.legend(loc='lower left')
plt.title('Select Wavefunctions for a Sinusoidal Potential on a Spatial Grid of 120 Points')
plt.show()
"""print('Eigenvalues', w[1:4])
print('Eigenvectors', v[1:4])"""

