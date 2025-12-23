import numpy as np
# simple array
array_simple=[1,2,3,4,5]
np_array_simple = np.array(array_simple)
print("Simple Array:",array_simple,type(array_simple))
print("Numpy Array from Simple Array:",np_array_simple,type(np_array_simple))

# nested array
array_nested=[[1,2,3],[4,5,6],[7,8,9]]
np_array_nested = np.array(array_nested)    
print("Nested Array:",array_nested,type(array_nested))
print("Numpy Array from Nested Array:",np_array_nested,type(np_array_nested))

# We can use Tuple instead of a list as well.
my_tuple = (-1,0,1)
my_array = np.array(my_tuple)
print(my_tuple, type(my_tuple) )
print( my_array, type(my_array) )

