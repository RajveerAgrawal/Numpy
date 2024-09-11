import numpy as np

array = np.linspace(0, 9, 10)
print("Original array:", array)

modified_array = np.where(array % 2 != 0, -1, array)
print("Modified array with odd numbers replaced by -1:", modified_array)

two_dim_array = array.reshape(2, -1)
print("2-dimensional array with two rows:\n", two_dim_array)

even_sum = np.sum(array[array % 2 == 0])
print("Sum of all even elements:", even_sum)