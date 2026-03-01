from flask import Flask, render_template, request
import pickle
import numpy as np

# create flask app
app = Flask(__name__)

# load trained ML model
model = pickle.load(open('model.pkl', 'rb'))

# home page
@app.route('/')
def home():
    return render_template('index.html')

# prediction function
@app.route('/predict', methods=['POST'])
def predict():

    # get values from form
    month = request.form['month']
    food = float(request.form['food'])
    rent = float(request.form['rent'])
    travel = float(request.form['travel'])
    shopping = float(request.form['shopping'])
    bills = float(request.form['bills'])

    # prediction using model
    prediction = model.predict([[food, rent, travel, shopping, bills]])

    output = round(prediction[0], 2)

    # send values back to html for graphs
    return render_template('index.html',
                           prediction_text="Predicted Total Expense: ₹" + str(output),
                           month=month,
                           food=food,
                           rent=rent,
                           travel=travel,
                           shopping=shopping,
                           bills=bills)

# run app
if __name__ == "__main__":
    app.run(debug=True)