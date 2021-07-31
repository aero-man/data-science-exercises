import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def calc_top_sale_price_correlations(houses, top=10):
    sale_price_correlations = houses.corr()["SalePrice"]
    abs_correlations = abs(sale_price_correlations)
    max_corr = abs_correlations.sort_values(ascending=False)    
    top_corr = max_corr[1:top+1] # ignore first correlation with self, which is 1:1
    return top_corr


houses = pd.read_csv("AmesHousing.txt", sep="\t")

print(houses.info())
print(houses.corr())
print(houses.corr()["SalePrice"])
print(f"Top predictors of sale price:\n{calc_top_sale_price_correlations(houses, 10)}")

train_houses= houses[:1460]
test_houses = houses[1460:]

# Simple Linear Regression
lr = LinearRegression()
lr.fit(train_houses[["Overall Qual"]], train_houses["SalePrice"])

train_predictions = lr.predict(train_houses[["Overall Qual"]])
test_predictions = lr.predict(test_houses[["Overall Qual"]])

train_mse = mean_squared_error(train_predictions, train_houses["SalePrice"])
test_mse = mean_squared_error(test_predictions, test_houses["SalePrice"])

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

print()
print("Simple Linear Regression: ")
print(f"Training data MSE: {train_mse}")
print(f"Training data RMSE: {train_rmse}")
print(f"Test data MSE: {test_mse}")
print(f"Test data MSE: {test_rmse}")

# Multiple Linear Regression
columns = ["Gr Liv Area", "Year Built"]
lr2 = LinearRegression()
lr2.fit(train_houses[columns], train_houses["SalePrice"])

train_predictions = lr2.predict(train_houses[columns])
test_predictions = lr2.predict(test_houses[columns])

train_mse = mean_squared_error(train_predictions, train_houses["SalePrice"])
test_mse = mean_squared_error(test_predictions, test_houses["SalePrice"])

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

print()
print("Multiple Linear Regression: ")
print(f"Training data MSE: {train_mse}")
print(f"Training data RMSE: {train_rmse}")
print(f"Test data MSE: {test_mse}")
print(f"Test data MSE: {test_rmse}")


