import joblib
from flask import Flask, render_template, request
from preprocess import preprocess_data
import numpy as np

app = Flask(__name__)

scaler = joblib.load('Models/scaler.h5')
model = joblib.load('Models/model.h5')


@app.route('/') 
def index() :
    return render_template('index.html')


@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    
    if request.method == 'POST' :
        wheelbase = request.form['wheelbase']
        curbweight = request.form['curbweight']
        cylindernumber = request.form['cylindernumber']
        enginesize = request.form['enginesize']
        horsepower = request.form['horsepower']
        highwaympg = request.form['highwaympg']
        fueltype = request.form['fueltype']
        aspiration = request.form['aspiration']
        drivewheel = request.form['drivewheel']
        enginetype = request.form['enginetype']
      
    data = {'wheelbase' : wheelbase, 'curbweight' : curbweight, 'cylindernumber' : cylindernumber, 
            'enginesize' : enginesize, 'horsepower' : horsepower, 'highwaympg' : highwaympg, 'fueltype' : fueltype
           ,"aspiration" : aspiration, "drivewheel" : drivewheel, "enginetype" : enginetype}
    
    final_data = preprocess_data(data)
    prediction = ["low cost","medium cost","high cost"]
    prediction = prediction[model.predict(scaler.transform([final_data]))[0]]
    # return str(round(prediction))
    return render_template('prediction.html', car_price = str((prediction)))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
