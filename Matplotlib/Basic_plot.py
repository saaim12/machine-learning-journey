import numpy as np
import matplotlib.pyplot as plt
# Simple graph to show the sin of values 
degrees = np.array([0, 30, 45, 90, 180])
radians = np.deg2rad(degrees)

sin_values = np.sin(radians)
print(sin_values)
plt.plot(degrees, sin_values, marker='o')
plt.title('Sine Function')
plt.show()
plt.scatter(degrees, sin_values, color='red')
plt.show()

# ============================
# scatter vs plt.plot (Matplotlib)
# ============================

# plt.scatter(x, y)
# - Shows individual data points only
# - DOES NOT connect points with lines
# - Order of data does NOT matter
# - Best for visualizing raw data, noise, outliers
# - Commonly used for training data in ML
#
# Example mental model:
# "Here are my data points"

# ------------------------------------------------

# plt.plot(x, y)
# - Connects points with a line
# - Order of data MATTERS
# - Best for showing trends, functions, predictions
# - Commonly used for model predictions, loss curves, time-series
#
# Example mental model:
# "Here is the trend / function / model"

# ------------------------------------------------

# ML Best Practice:
# - Use scatter for actual data
# - Use plot for predicted values
#
# Example:
# plt.scatter(x_train, y_train)   # actual data
# plt.plot(x_train, y_pred)       # model prediction

# ------------------------------------------------

# Common mistake:
# - Using plt.plot() for unordered raw data
#   This can create a misleading trend

# ------------------------------------------------

# Summary:
# scatter -> raw data visualization
# plot    -> trend / prediction / function
