from flask import Flask , render_template, url_for, request
import joblib

import pandas as pd 
model = joblib.load('RD_model.lb')
app = Flask(__name__)


@app.route('/')                    # (/) --> home route 
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactus():
    return render_template('contact.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        brand_name = request.form['brand_name']
        owner_name=int(request.form['owner'])
        age_bike=int(request.form['age'])
        power_bike= int(request.form['power'])
        kms_driven_bike= int(request.form['kms_driven'])
        bike_numbers={'TVS': 0,
                        'Royal Enfield': 1,
                        'Triumph': 2,
                        'Yamaha': 3,
                        'Honda': 4,
                        'Hero': 5,
                        'Bajaj': 6,
                        'Suzuki': 7,
                        'Benelli': 8,
                        'KTM': 9,
                        'Mahindra': 10,
                        'Kawasaki': 11,
                        'Ducati': 12,
                        'Hyosung': 13,
                        'Harley': 14,
                        'Jawa': 15,
                        'BMW': 16,
                        'Indian': 17,
                        'Rajdoot': 18,
                        'LML': 19,
                        'Yezdi': 20,
                        'MV': 21,
                        'Ideal': 22}
        
        brand_name_encode=bike_numbers[brand_name]
        lst=[[owner_name,brand_name_encode,kms_driven_bike,age_bike,power_bike]]  #sequence order
        pred = model.predict(lst)
        pred = pred[0]
        pred = round(pred, 2)
        user_data = (str(owner_name),str(brand_name),kms_driven_bike,age_bike,power_bike,pred)
        return render_template("project.html",prediction=str(pred))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=2525,debug=True)
    # debug
