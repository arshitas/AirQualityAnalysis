## Air Quality Analysis

This Machine Learning model analyses the air quality standards by using regression algorithms. Carbon and Nitrogen oxides are identified as major air pollutants and hence seperate analysis is performed. The dataset is retrieved from [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/index.php) and is preprocessed/cleaned before applying in the model. We also use this data to compare three different regression algorithms, namely ***Multiple Linear regression, Ridge regression and Lasso regression*** and ***the effect of varying the regularization parameter in Ridge regression***.

### Data Set Information
The dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level,within an Italian city. The dataset includes missing values as well as the value of -200 is returned when the machine is unable to detect for some reasons. 

### Python Libraries
* Numpy 
* Pandas
* Scikit learn
* Matplotlib

### ML model
* The regression model developed for analyzing Carbon emission derives the relation between CO emission to NMHC and benzene concentration. The model compares between Multiple, Ridge and Lasso regression by using R-squared value.
* The regression model developed for analyzing Nitrogen emission uses Ridge regression to map the relation between NOx and NO2 concentration. Here we change the value of regularization parameter and observe in effects by the R-squared value.

### Output
From carbon oxide analysis:
```
**Multiple Linear Regression**
Coefficient : [[0.0004174  0.17347891]],Intercept: [0.38442317]
R2 score training set :  0.9478911454330675
R2 score test set     :  0.944181955784372 


**Ridge Regression**
Coefficient : [[0.00041818 0.17345491]],Intercept: [0.38450433]
R2 score training set :  0.947891142052559
R2 score test set     :  0.944182860919876 


**Lasso Regression**
Coefficient : [0.00307137 0.09042445],Intercept: [0.67073315]
R2 score training set :  0.9073918014903195
R2 score test set     :  0.9205034706780072 
```

The predicted value of test set are plotted against actual values: 
![](https://github.com/arshitas/AirQualityPrediction/blob/main/OutputFiles/LinearReg.png)


From Nitrogen oxide analysis:
```
**Ridge Regression**

Alpha = 0.00
 R-squared training = 0.7249371838045687, R-squared test = 0.7664067347059627

Alpha = 1.00
 R-squared training = 0.7249371838027381, R-squared test = 0.7664066177489275

Alpha = 10.00
 R-squared training = 0.7249371836215083, R-squared test = 0.7664055649942845

Alpha = 100.00
 R-squared training = 0.7249371655037544, R-squared test = 0.766395023461202

Alpha = 1000.00
 R-squared training = 0.724935358945858, R-squared test = 0.7662882141579181
 ```
 The matplotib figures are obtained for different values of alpha :
 ![](https://github.com/arshitas/AirQualityPrediction/blob/main/OutputFiles/Alpha_1.png)
 
 ![](https://github.com/arshitas/AirQualityPrediction/blob/main/OutputFiles/Alpha_100.png)
 
 ![](https://github.com/arshitas/AirQualityPrediction/blob/main/OutputFiles/Alpha_1000.png)
 
 ### Conclusion
 The multiple regression and ridge regression have proved to better in explaining the variation of CO when compared to Lasso regression. Large values of R-square explain the dependency of CO emission on NMHC and Benzene concentration in air.
 
The nitrogen analysis explains that NO2 is the most signinficant of all NOx emission. Increasing the regularization parameter alpha show negligible effect on the training set score but show decreasing trend on test set.
(Note that the conclusions are based on AirQuality dataset only and does not imply for the general comparisons between algorithms.)
