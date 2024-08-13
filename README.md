## House Price Prediction Flask Application ##

## Project Overview
This Flask web application predicts house prices based on input features using a machine learning model. Users can input details such as the number of bedrooms, bathrooms, size in square feet, and location to get a predicted price.

## my_flask_project_structure
├── static/
│ ├── house.jpg # Background image for the application
│ ├── style.css # CSS styles for the application
├── templates/
│ ├── form.html # HTML form for user input
│ └── result.html # HTML page to display prediction results
├── app.py # Main Flask application file
├── train_model.py # Script to train the machine learning model
├── requirements.txt # List of dependencies
└── README.md # Documentation file

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: python -m venv venv
3. Activate the virtual environment:
   - On Windows: venv\Scripts\activate
4. Install dependencies: pip install -r requirements.txt
5. Run the application: python app.py

## Dependencies
Flask: Web framework for Python.
scikit-learn: Machine learning library.
pandas: Data manipulation and analysis library.
numpy: Numerical computing library.

## Usage Instructions
Open your web browser and go to http://localhost:5000.
Fill out the form with house features (e.g., number of bedrooms, bathrooms, size in square feet, and location).
Click the "Predict" button to submit the form.
View the predicted house price displayed on the result page.

## License
This project is licensed under the MIT License.