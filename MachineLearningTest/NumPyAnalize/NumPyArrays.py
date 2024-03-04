import numpy as np

# array

np.array([1, 2, 3])


odd_number_list = [1, 3, 5 ,7]
np.array(odd_number_list)

two_dim_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
np.array(two_dim_list)

# arange

np.arange(0, 10)
np.arange(0, 10, 2)

# zeros

np.zeros(9)
np.zeros((2, 3)) #"matrisa"
np.zeros((3, 2)) #"matrisa"

# ones

np.ones(3)
np.ones((2, 3)) #"matrisa"
np.ones((3, 2)) #"matrisa"

# linspace

np.linspace(0, 10, 5)
np.linspace(0, 5, 10)

# Eye

np.eye(3) #"matrisa"
np.eye(9) #"matrisa"

# Random (rand, randn, randint)

np.random.rand(3)
np.random.rand(7)
np.random.rand(3, 4)

np.random.randn(3)
np.random.randn(5)
np.random.randn(3, 5)

np.random.randint(0, 50, 20)

rand_arr = np.random.randint(0, 50 ,20)
rand_arr

second_arr = np.arange(20)
second_arr

# Reshape

rand_arr.reshape(4, 5)
rand_arr.reshape(5, 5) # error 20 into shape

# Max Min

second_arr.max()
second_arr.min()

second_arr.argmax()

rand_arr.max()
rand_arr.argmax()

rand_arr.min()
rand_arr.argmin()

second_arr.shape

reshaped_arr = second_arr.reshape(2, 10)
reshaped_arr

reshaped_arr.shape
reshaped_arr.dtype












