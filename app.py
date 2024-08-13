from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('models/model.pkl')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    size = float(request.form['size'])
    location = request.form['location']

    input_data = pd.DataFrame([[bedrooms, bathrooms, size, location]], columns=['bedrooms', 'bathrooms', 'size', 'location'])

    input_data = pd.get_dummies(input_data, columns=['location'], drop_first=True)

    expected_columns = ['bedrooms', 'bathrooms', 'size', 'location_Suburb', 'location_Urban']
    for column in expected_columns:
        if column not in input_data.columns:
            input_data[column] = 0

    input_data = input_data[expected_columns]

    predicted_price_usd = model.predict(input_data)[0]

    conversion_rate = 82   

    predicted_price_inr = predicted_price_usd * conversion_rate

    return render_template('result.html', price=predicted_price_inr)

if __name__ == '__main__':
    app.run(debug=True)
