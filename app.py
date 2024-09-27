from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Sample weather dataset (Temperature, Humidity, Wind Speed, Rain)
data = {
    'Temperature': [30, 25, 20, 35, 18, 28, 22, 24, 26, 31],
    'Humidity': [70, 65, 90, 50, 80, 60, 85, 75, 65, 55],
    'Wind Speed': [12, 8, 10, 15, 5, 9, 14, 6, 10, 13],
    'Rain': [1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['Temperature', 'Humidity', 'Wind Speed']]
y = df['Rain']

# Train Decision Tree model
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    wind_speed = float(request.form['wind_speed'])

    # Create input array for prediction
    input_data = np.array([[temperature, humidity, wind_speed]])

    # Perform prediction
    prediction = dt_classifier.predict(input_data)[0]

    # Return prediction result
    if prediction == 1:
        result = "Yes, it will rain."
    else:
        result = "No, it will not rain."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
