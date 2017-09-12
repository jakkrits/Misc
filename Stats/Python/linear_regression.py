""" Linear Regression Analysis - HW#1 - JakkritS  """
#%%
import statsmodels.api as StatModel
## import datasets from sckit-learn
from sklearn import datasets, linear_model

import numpy
import pandas

## loads Boston dataset from datasets library
data = datasets.load_boston() 
# print(data.feature_names)
# print(data.target)

# define the data/predictors as the pre-set feature names
dataFrame = pandas.DataFrame(data.data, columns=data.feature_names)
# print(dataFrame)
target = pandas.DataFrame(data.target, columns=["MEDV"])

# X1 = dataFrame["RM"]
# Y1 = target["MEDV"]

# model1 = StatModel.OLS(Y1, X1).fit()
# redictions1 = model1.predict(X1)

# model1.summary()

X2 = dataFrame[["RM", "LSTAT"]]
y2 = target["MEDV"]
# model2 = StatModel.OLS(y2, X2).fit()
# predictions2 = model2.predict(X2)
# model2.summary()
# print(data)

lm = linear_model.LinearRegression()
model3 = lm.fit(X2, y2)
predictions3 = lm.predict(X2)
print(predictions3)[0:5]