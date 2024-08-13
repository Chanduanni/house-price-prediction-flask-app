import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv('simplified_housing.csv')

X = data[['bedrooms', 'bathrooms', 'size', 'location']]
y = data['price']

X = pd.get_dummies(X, columns=['location'], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'models/model.pkl')
