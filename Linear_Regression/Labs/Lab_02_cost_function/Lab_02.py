import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)

# Cost function
def compute_cost(x, y, w, b, m):
    total_cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        total_cost += (y[i] - f_wb) ** 2
    return total_cost / (2 * m)

m = len(x)

# Example parameters
w = 1
b = 2

# Compute cost
cost = compute_cost(x, y, w, b, m)
print("Cost at w =", w, ", b =", b, "is", cost)

# Plotting data points
plt.scatter(x, y, color='blue', label='Data points')

# Plotting model line f(x) = w*x + b
y_pred = w * x + b
plt.plot(x, y_pred, color='red', label='Model line')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Data points and Model Line")
plt.legend()
plt.show()
## as we can see how the cost function changes with different values of w and b.
# You can modify w and b to see how the cost changes
w = 0.5
b = 1
cost = compute_cost(x, y, w, b, m)
print("Cost at w =", w, ", b =", b, "is", cost)
y_pred = w * x + b
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='green', label='Model line (w=0.5, b=1)')
plt.legend()
plt.show()
## This code computes the cost function for a simple linear regression model and visualizes the data points along with the model line for different parameters w and b.
w_values = np.linspace(-1, 3, 50)
cost_values = [compute_cost(x, y, w, b=2, m=m) for w in w_values]

plt.plot(w_values, cost_values, color='purple')
plt.xlabel("w")
plt.ylabel("Cost")
plt.title("Cost vs w (b=2)")
plt.show()
