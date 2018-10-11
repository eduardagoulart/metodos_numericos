import numpy as np

A = np.array([[2.0, 1.0, -1.0],
         [-2.0, 1.0, 2.0],
         [-3.0, -1.5, 2.0]])
B = np.array([[8], [-3], [-11]])

A_inversa = np.linalg.inv(A)

X = np.dot(A_inversa, B)

