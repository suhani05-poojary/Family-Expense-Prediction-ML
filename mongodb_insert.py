from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database
db = client["family_expense_db"]

# Create collection
collection = db["expenses"]

# Load JSON file
with open("expenses.json") as file:
    data = json.load(file)

# Delete old data
collection.delete_many({})

# Insert new data
collection.insert_many(data)

print("Data inserted into MongoDB successfully!")