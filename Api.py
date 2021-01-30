from flask import Flask,request
from flask_cors import CORS, cross_origin
import joblib
import numpy as np



app = Flask(__name__)
CORS(app)

@app.route('/')
def helloworld():
    return 'HellowWorld'


@app.route('/area') #ถ้าไม่ใส่ method default = GET
@cross_origin() #แก้ cross origin เวลารันข้าม domain
def area():
    w = float(request.values['w'])
    h = float(request.values['h'])

    return str(w*h)
# http://localhost:5000/area?w=40&h=2 


@app.route('/bmi', methods=['POST'])
@cross_origin() #แก้ cross origin เวลารันข้าม domain
def bmi():
    weight = float(request.values['w']) #kg
    height = float(request.values['h']) #cm

    height = height/100
    bmi = weight/(height**2)

    return str(bmi) #ครอบเป็น str เสมอ

@app.route('/iris', methods=['GET','POST'])
@cross_origin() #แก้ cross origin เวลารันข้าม domain
def predict_species():
    model = joblib.load("iris.model")
    req = request.values['param']
    inputs = np.array(req.split(','), dtype = np.float32).reshape(1,-1)
    predict_target = model.predict(inputs)

    if predict_target == 0:
        return 'Settosa'
    elif predict_target == 1:
        return 'Vergicolor'
    else:
        return 'Virginica'
# http://localhost:5000/iris?param=5.1,3.5,1.4,0.2  --> GET Method
   



if __name__ =='__main__':
    app.run(host = '0.0.0.0', port=5000, debug =True) #debug = true คือ auto refresh 