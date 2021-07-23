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
X = data[['NO2(GT)']]
y= data[['NOx(GT)']]

X_train, X_test, y_train, y_test =train_test_split(X,y,random_state=0)

#step 4: Applying Ridge regression as a function of alpha
print('\n**Ridge Regression**\n')
for a in [0,1,10,100,1000]:
    linridge = Ridge(alpha=a).fit(X_train,y_train)
    print('Alpha = {:.2f}\n R-squared training = {}, R-squared test = {}\n\n'.format(a, linridge.score(X_train,y_train),linridge.score(X_test,y_test)))
    plt.scatter(X, y, marker= 'o', c='g',s=50, alpha=0.8)
    plt.plot(X, linridge.coef_ * X + linridge.intercept_, 'r-')
    plt.title('Ridge regression - alpha = {:.2f}'.format(a))
    plt.xlabel('Feature value (NO2)')
    plt.ylabel('Target value (NOx)')
    plt.show()
    
