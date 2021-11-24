from flask import Flask,request, url_for, redirect, render_template  ## importing necessary libraries
import pickle  ## pickle for loading model(Diabetes.pkl)
import pandas as pd  ## to convert the input data into a dataframe for giving as a input to the model
import numpy as np


app = Flask(__name__)  ## setting up flask name

model = pickle.load(open("Diabetes3.pkl", "rb"))  ##loading model

@app.route('/')             ## Defining main index route
def home():
    return render_template("index.html")   ## showing index.html as homepage


@app.route('/predict',methods=['POST','GET'])  ## this route will be called when predict button is called
def predict(): 
    #int_features=[float(x) for x in request.form.values()]
    text1 = request.form['1']      ## Fetching each input field value one by one
    text2 = request.form['2'] 
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    
    colms=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    row_df = pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7,text8],index=colms)])  ### Creating a dataframe using all the values
    print(row_df)
    # print(row_df.info())
    for i in colms:
        row_df[i] = pd.to_numeric(row_df[i])
    
    def impute_data(df):
        col=['Glucose', 'BloodPressure','BMI']
        for i in col:
            df[i].replace(0, np.nan, inplace= True)
        df.loc[(df['Glucose'].isnull()), 'Glucose'] = 117
        df.loc[(df['BloodPressure'].isnull()), 'BloodPressure'] = 72
        df.loc[(df['BMI'].isnull()), 'BMI'] = 32.45
        return df

    row_df = impute_data(row_df)
    print(row_df)
    
    # print(row_df.info())
    prediction=model.predict_proba(row_df) ## Predicting the output
    output='{0:.{1}f}'.format(prediction[0][1], 2)    ## Formating output

    if output>str(0.5):
        return render_template('index.html',pred='You have chance of having diabetes.\nProbability of having Diabetes is {}'.format(output)) ## Returning the message for use on the same index.html page
    else:
        return render_template('index.html',pred='You are safe.\n Probability of having diabetes is {}'.format(output)) 
    
    
    
# if __name__ == '__main__':
#     app.run(debug=True)          ## Running the app as debug==True

# For docker 
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)          ## Running the app as debug==True