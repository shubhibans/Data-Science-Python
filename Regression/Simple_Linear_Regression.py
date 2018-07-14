# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 02:34:58 2018

@author: shubh
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,1].values


from sklearn.model_selection import train_test_split
X_train, X_test, Y_Train, Y_test= train_test_split(X, Y, test_size=1/3, random_state= 0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, Y_Train)

y_pred=regressor.predict(X_test)



plt.scatter(X_train, Y_Train, color="red" )
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test, Y_test, color="red" )
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
