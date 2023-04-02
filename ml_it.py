# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:54:30 2023

@author: Gabriel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def ml(val):   
    # Load data
    data = pd.read_csv(r"D:\flaskproject\used_cars.csv")
    
    # Create X and y arrays
    X = data['mileage'].values.reshape(-1,1)
    y = data['price'].values.reshape(-1,1)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Create linear regression model
    model = LinearRegression()
    
    # Fit the model using the training data
    model.fit(X_train, y_train)
    
    # Predict the prices of the testing data using the model
    y_pred = model.predict(X_test)
    pred = model.predict([[val]])
    print(pred)
    # Visualize the training data and model predictions
    plt.scatter(X_train, y_train, color='blue')
    plt.plot(X_test, y_pred, color='red')
    plt.title('Mileage vs Price (Training Data)')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.show()
    
    # Calculate the R-squared value
    r_squared = model.score(X_test, y_test)
    #print('R-squared value:', r_squared)
