## Air Quality Analysis

This Machine Learning model analyses the air quality standards by using regression algorithms. Carbon and Nitrogen are identified as the two major pollutants and hence seperate analysis is done for both the elements. The dataset is retrieved from [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/index.php) and is preprocessed/cleaned to be applied in the model. We also use this data to compare three different regression algorithms, namely ***Multiple Linear regression, Ridge regression and Lasso regression*** and ***the effect of varying the regularization parameter in Ridge regression***.

### Data Set Information
The dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level,within an Italian city. The dataset includes missing values as well as the value of -200 is returned when the machine is unable to detect for some reasons. 

### Attribute Information 
0 Date (DD/MM/YYYY)  
1 Time (HH.MM.SS)  
2 True hourly averaged concentration CO in mg/m^3 (reference analyzer)  
3 PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)  
4 True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 (reference analyzer)  
5 True hourly averaged Benzene concentration in microg/m^3 (reference analyzer)  
6 PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted)  
7 True hourly averaged NOx concentration in ppb (reference analyzer)  
8 PT08.S3 (tungsten oxide) hourly averaged sensor response (nominally NOx targeted)  
9 True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)  
10 PT08.S4 (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)  
11 PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted)  
12 Temperature in Â°C  
13 Relative Humidity (%)  
14 AH Absolute Humidity  

### Python Libraries
* Numpy 
* Pandas
* Scikit learn
* Matplotlib.pyplot

### Application
The model is capable of predicting future values of carbon and nitrogen levels and hence alert the respected region of the country. 

### ML model
* The regression model developed for analyzing Carbon emission derives the relstion between CO emission to NMHC and benzene concentration. The model compares between Multiple, Ridge and Lasso regression by using R-squared value.
* The regression model developed for analyzing Nitrogen emission uses Ridge regression to map the relation between NOx and NO2 concentration. Here we change the value of regularization parameter and observe in effects by the R-squared value.

### Output
From carbon level analysis:
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
From Nitrogen level analysis:
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
 
 ### Matplotlib Figures
 
 ### Conclusion
