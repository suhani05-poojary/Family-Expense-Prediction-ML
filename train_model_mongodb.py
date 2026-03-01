from pymongo import MongoClient
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["family_expense_db"]
collection = db["expenses"]

# Get data
data = list(collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

# Remove _id column
if "_id" in df.columns:
    df.drop("_id", axis=1, inplace=True)

# Use only expense columns (NOT month)
X = df[['food', 'rent', 'travel', 'shopping', 'bills']]
y = df['total_expense']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model retrained successfully!")