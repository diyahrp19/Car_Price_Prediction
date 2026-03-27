import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset for car price prediction
data = pd.DataFrame({
    'year': [2010, 2015, 2012, 2018, 2020, 2013, 2016, 2011, 2019, 2014],
    'mileage': [150000, 80000, 120000, 40000, 20000, 110000, 70000, 130000, 30000, 90000],
    'engine_size': [1.6, 2.0, 1.8, 2.2, 2.0, 1.6, 2.4, 1.8, 2.0, 1.6],
    'horsepower': [110, 150, 130, 180, 200, 120, 160, 115, 190, 140],
    'doors': [4, 4, 4, 2, 4, 4, 4, 2, 4, 4],
    'price': [5000, 12000, 8000, 18000, 25000, 7000, 15000, 6000, 22000, 10000]
})

X = data[['year', 'mileage', 'engine_size', 'horsepower', 'doors']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('car_model.pkl', 'wb'))

print("Car Price Model trained and saved!")