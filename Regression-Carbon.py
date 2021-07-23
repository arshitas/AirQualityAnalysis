import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import matplotlib.pyplot as plt

#step 1: reading the values from csv file
df= pd.read_csv(r'C:\Users\Ravindra Nath Shukla\Downloads\AirQualityUCI.csv',delimiter= ';',decimal =',')
print('**Air Quality Data**\n')
print(df.head(15))

#step 2: preprocessing feature set
df= df[['Date', 'Time', 'CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)', 'C6H6(GT)',
       'PT08.S2(NMHC)', 'NOx(GT)', 'PT08.S3(NOx)', 'NO2(GT)', 'PT08.S4(NO2)',
       'PT08.S5(O3)', 'T', 'RH', 'AH']]

data = df.replace(to_replace = -200, value = np.nan)
data.dropna(inplace=True)

#step 3: dividing the data set into training and test set
#traing set and test set ratio = 75:25
X = data[['NMHC(GT)','C6H6(GT)']]
y= data[['CO(GT)']]

X_train, X_test, y_train, y_test =train_test_split(X,y,random_state=0)

#step 4: Applying multiple linear regression
ols= LinearRegression()
ols.fit(X_train,y_train)
print('\n**Multiple Linear Regression**')
print('Coefficient : {},Intercept: {}'.format(ols.coef_,ols.intercept_))
print('R2 score training set : ',ols.score(X_train,y_train))
print('R2 score test set     : ',ols.score(X_test,y_test),'\n\n')

y_lin = ols.predict(X_test)
plt.scatter(y_test,y_lin)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Multiple Linear Regression : Actual vs Predicted')
plt.show()

#step 5: Applying Ridge regression
linridge = Ridge(alpha=1.0).fit(X_train,y_train)
print('**Ridge Regression**')
print('Coefficient : {},Intercept: {}'.format(linridge.coef_,linridge.intercept_))
print('R2 score training set : ',linridge.score(X_train,y_train))
print('R2 score test set     : ',linridge.score(X_test,y_test),'\n\n')
y_ridge = linridge.predict(X_test)

plt.scatter(y_test,y_ridge)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Ridge Regression : Actual vs Predicted')
plt.show()

#step 6: Applying Lasso Regression
linlasso = Lasso(alpha=1.0).fit(X_train,y_train)
print('**Lasso Regression**')
print('Coefficient : {},Intercept: {}'.format(linlasso.coef_,linlasso.intercept_))
print('R2 score training set : ',linlasso.score(X_train,y_train))
print('R2 score test set     : ',linlasso.score(X_test,y_test),'\n\n')
y_lasso = linlasso.predict(X_test)
plt.scatter(y_test,y_lasso)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Lasso Regression : Actual vs Predicted')
plt.show()

