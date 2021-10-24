# Diabetic-detection

## Motivation:
To grow my machine learning skills, this is another continuation of my ML project - diabetes prediction. 
In this project, we did the following:
1) Exploratory data analysis (EDA)
2) Building ML project
3) Prepare a webapps and Deploy this in Heroku  

Here is our webapps access link <a href="https://diabetic-detection-app-rashed.herokuapp.com/">https://diabetic-detection-app-rashed.herokuapp.com</a>   
Webapps homepage looks like in below after deploying it in heroku.

<!-- ![Alt Text](https://github.com/rashed2940/Diabetic-detection/blob/main/charts/apps.gif) -->

<p align="center">
<img src="/charts/apps.gif"   title = "WebApps Home Page">
</p>



## DataSet Description:
According to WHO about 422 million people worldwide have diabetes. Since diabetes affects a large population across the globe and the collection of these datasets is a continuous process and it comprises of various patient related attributes such as age, gender, symptoms, insulin levels, blood pressure, blood glucose levels, weight etc. We are working on Pima Indians Diabetes Dataset (PIDD), extracted from <a href="https://www.kaggle.com/uciml/pima-indians-diabetes-database">Kaggle.</a>

This dataset consists of multiple independent variables and one dependent variable (Outcome). Independent variables include:

1) Pregnancies: Number of times pregnant
2) Glucose: Plasma Glucose Concentration a 2-hour in an Oral Glucose Tolerance Test (mg/dl).
3) BloodPressure: Diastolic Blood Pressure (mm/Hg).
4) SkinThickness: Triceps Skin Fold Thickness (mm)
5) Insulin: 2-Hour Serum Insulin (mu U/ml)
6) BMI: Body Mass Index (weight in kg/(height in m)^2)
7) DiabetesPedigreeFunction: It provides information about diabetes history in relatives and genetic relationship of those relatives with patients. Higher Pedigree Function means patient is more likely to have diabetes.
8) Age: Age of an individual (years)
9) Outcome: Target Variable (0 or 1) where ‘0’ denotes patient is not diabetic and ‘1’ denotes patient is diabetic.

## EDA Analysis:

There 5 obserbations are extracted from given data

- Healthy persons are concentrate with an age <= 30 and glucose <= 120

  <p align="center">
  <img src="/charts/tmp/gvsa.png"   title = "Glucose Vs Age">
  </p>
  
- Healthy persons are concentrate with an age <= 30 and no of pregnancies <=6
  
  <p align="center">
  <img src="/charts/tmp/pvsa.png"   title = "Pregnancy Vs Age">
  </p>
  
 - Healthy persons are concentrate with a Blood pressure <= 80 and glucose <= 105
  
  <p align="center">
  <img src="/charts/tmp/gvsbp.png"   title = "Glucose Vs Blood Pressure">
  </p>
  
  - Healthy persons are concentrate with a BMI < 30 and skinthickness <= 20
  
  <p align="center">
  <img src="/charts/tmp/BMIvsST.png"   title = "BMI Vs skinthickness">
  </p>
  
  - Healthy persons are concentrated below BMI < 40 and Glucose < 150
  
  <p align="center">
  <img src="/charts/tmp/gvsBMI.png"   title = "BMI Vs Glucose">
  </p>

