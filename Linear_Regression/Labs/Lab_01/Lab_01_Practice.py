import numpy as np
import matplotlib.pyplot as plt
# Sample data
# X --> input , feature, 
# Y --> output ,target values
np.random.seed(42)  # for reproducibility
# Generate 50 house sizes between 500 and 3000 sq ft
x_train = np.random.randint(500, 3000, size=50)
# Generate prices (roughly $100–300 per sq ft + noise)
y_train = np.random.randint(100, 300, size=50)
print("x_train (sq ft):", x_train)
print("y_train (price in dollars):", y_train)

# m is the number of training examples
m=len(x_train)
print("Number of training examples:", m)

# Visualizing the data
# plt.scatter(x_train,y_train,color='blue',marker='o',s=30)
# plt.xlabel('Size of house (sq ft)')
# plt.ylabel('Price of house (dollars)')
# plt.title('House Prices vs. Size')
# plt.show()


# now function of model is
# f(x) = w*x + b
def model(x, w, b):
    return w * x + b
# Example parameters (initial guess)
w = 0.2
b = 0.3

# Predictions
y_pred = model(x_train, w, b)

# Plot model prediction
plt.scatter(x_train, y_train, label="Training Data")
plt.plot(x_train, y_pred, color='red', label="Model Prediction")
plt.legend()
plt.show()