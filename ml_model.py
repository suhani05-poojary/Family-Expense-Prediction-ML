from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["family_expense_db"]
collection = db["expenses"]

data = list(collection.find())
df = pd.DataFrame(data)

if "_id" in df.columns:
    df.drop("_id", axis=1, inplace=True)

X = df[["month", "food", "rent", "travel", "shopping", "bills"]]
y = df["total_expense"]

model = LinearRegression()
model.fit(X, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    month = float(request.form["month"])
    food = float(request.form["food"])
    rent = float(request.form["rent"])
    travel = float(request.form["travel"])
    shopping = float(request.form["shopping"])
    bills = float(request.form["bills"])

    user_input = [[month, food, rent, travel, shopping, bills]]
    prediction = model.predict(user_input)

    return render_template("index.html",
                           prediction_text=f"Predicted Expense: {round(prediction[0],2)}")

if __name__ == "__main__":
    app.run(debug=True)