import numpy as np

# ------------------------
# np.arange(start, stop, step)
# ------------------------
# - Generates numbers from start (inclusive) to stop (exclusive)
# - Uses a fixed step size between numbers
# - Stop value may NOT be included exactly
# - Good when you know the "step size" you want

arr1 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# ------------------------
# np.linspace(start, stop, num)
# ------------------------
# - Generates 'num' evenly spaced numbers between start and stop
# - Stop value IS included by default
# - Good when you know how many points you want
# - Step size is automatically calculated

arr2 = np.linspace(0, 10, 20)  # [0., 2.5, 5., 7.5, 10.]

# ------------------------
# Key Differences
# ------------------------
# 1. np.arange → fixed step size, stop may be excluded
# 2. np.linspace → fixed number of points, stop included
# 3. np.linspace is preferred in ML for plotting smooth curves
print(arr2)