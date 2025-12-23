# ===============================
# NumPy basics for Machine Learning
# ===============================

# Import NumPy and give it the standard alias "np"
# Everyone does this. There is no rebellion here.
import numpy as np


# -------------------------------
# Creating arrays
# -------------------------------

# arange creates values starting from 1 up to (but not including) 10
# dtype=int forces integer values
arange_arr = np.arange(1, 10, dtype=int)

# randint creates random integers
# 1  -> inclusive lower bound
# 12 -> exclusive upper bound
# 10 -> number of elements
randint_arr = np.random.randint(1, 12, 10, dtype=int)

print("Array using arange:", arange_arr)
print("Array using randint:", randint_arr)


# -------------------------------
# Reshaping arrays
# -------------------------------

# reshape changes the shape of the array without changing data
# IMPORTANT RULE:
# rows × columns MUST equal total number of elements
print("----------- Reshape Example -----------")
reshaped_arr = arange_arr.reshape(3, 3)
print(reshaped_arr)


# -------------------------------
# Another random array
# -------------------------------

# Create an array of 10 random integers between 0 and 99
array_randint = np.random.randint(0, 100, 10)
print("Random array:", array_randint)


# -------------------------------
# Finding max and min values
# -------------------------------

# max() returns the largest value in the array
print("Maximum value:", array_randint.max())

# min() returns the smallest value in the array
print("Minimum value:", array_randint.min())


# -------------------------------
# Finding index of max and min
# -------------------------------

# argmax() returns the INDEX of the maximum value
# Indexing in Python starts from 0
print("Index of maximum value:", array_randint.argmax())

# argmin() returns the INDEX of the minimum value
print("Index of minimum value:", array_randint.argmin())


# -------------------------------
# Array attributes (metadata)
# -------------------------------

# size -> total number of elements in the array
print("Size:", array_randint.size)

# shape -> dimensions of the array
# For ML, usually (n_samples, n_features)
print("Shape:", array_randint.shape)

# dtype -> data type of elements stored in the array
# Important for memory and ML models
print("Data type:", array_randint.dtype)


# shape explanation example
print("----------- Shape Explanation -----------")
a = np.arange(10)

print(a.shape)                 # (10,)
print (a)
print(a.reshape(10, 1).shape)  # (10, 1)
print (a.reshape(10, 1))
print(a.reshape(1, 10).shape)  # (1, 10)
print (a.reshape(1, 10))
# Note how the total number of elements (10) remains the same
# Why ML cares a lot about this
# Scikit-learn expects:
# Features → columns
# Samples → rows
# So:
# One feature, 10 samples → (10, 1)
# One sample, 10 features → (1, 10)
# Get this wrong and sklearn throws errors that sound personal.
# Shape --->> (rows,cols) --->> (samples, features)
# -------------------------------
