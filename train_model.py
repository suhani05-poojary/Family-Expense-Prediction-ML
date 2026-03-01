import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("expenses.csv")

# Define input features (X)
X = data[['month', 'food', 'rent', 'travel', 'shopping', 'bills']]

# Define target variable (y)
y = data['total_expense']

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save trained model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully and model.pkl file created!")