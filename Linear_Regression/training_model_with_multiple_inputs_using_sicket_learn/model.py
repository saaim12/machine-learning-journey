from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load data
data = pd.read_csv('Advertising.csv')
X = data[['TV', 'radio', 'newspaper']]
y = data['sales']

# Split data 
# this will make sure that 20% of data is used for training and 80% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.2, test_size=0.8, random_state=42
)

# training model
model = LinearRegression()
model.fit(X_train, y_train)

# saving model as a file
joblib.dump(model, "linear_regression_advertising.pkl")
print("Model saved as linear_regression_advertising.pkl")

# Load model
loaded_model = joblib.load("linear_regression_advertising.pkl")
if loaded_model:
    print("Model loaded successfully.")
    

# predicting
y_pred = loaded_model.predict(X_test)

# evaluating
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# plotting actual vs predicted
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         'r--')
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()

# Joblib is a Python library used to save and load trained machine-learning models efficiently.
# It is optimized for NumPy arrays, which makes it ideal for scikit-learn models