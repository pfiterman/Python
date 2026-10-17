# Numpy
import numpy as np

# The zeros() function inside numpy creates an array with n number of zeroes inside it.
a = np.zeros(10)
print(a) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# The full() function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.
b = np.full((2,10), 0.7) 
print(b) # [[0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7],[0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]]

# The linspace() function generates 7 equally spaced values between 0 and 25, including both endpoints. The resultant array is printed in the output.
c = np.linspace(0,25,7) 
print(c) # [ 0.          4.16666667  8.33333333 12.5        16.66666667 20.83333333  25.        ]

# Finally, when you check the type of c, it is a special data type called ndarray (short for "n-dimensional array"), 
# which is the fundamental object used in numpy. This data type is much more efficient than a Python list and is optimized for numerical computations.
print(type(c))