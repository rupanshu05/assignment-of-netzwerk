import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify
import sklearn

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def results():
      Sales_in_thousands = float(request.form['Sales_in_thousands'])
      __year_resale_value = float(request.form['__year_resale_value'])
      Engine_size = float(request.form['Engine_size'])
      Horsepower = float(request.form['Horsepower'])
      Wheelbase = float(request.form['Wheelbase'])
      Width = float(request.form['Width'])
      Length = float(request.form['Length'])
      Curb_weight = float(request.form['Curb_weight'])
      Fuel_capacity = float(request.form['Fuel_capacity'])
      Model_Towncar = int(request.form['Model_Towncar'])
      Model_V40 = int(request.form['Model_V40'])
      Model_V70 = int(request.form['Model_V70'])
      Model_Villager = int(request.form['Model_Villager'])
      Model_Viper = int(request.form['Model_Viper'])
      Model_Voyager = int(request.form['Model_Voyager'])
      Model_Windstar = int(request.form['Model_Windstar'])
      Model_Wrangler = int(request.form['Model_Wrangler'])
      Model_Xterra = int(request.form['Model_Xterra'])
      Vehicle_type_Passenger = int(request.form['Vehicle_type_Passenger'])

      X = np.array([[Sales_in_thousands, __year_resale_value ,Engine_size , Horsepower , Wheelbase, Width , Length, Curb_weight , Fuel_capacity , Model_Towncar , Model_V40 , Model_V70 , Model_Villager , Model_Viper, Model_Voyager , Model_Windstar , Model_Wrangler , Model_Xterra, Vehicle_type_Passenger ,]])
      model = pickle.load(open('model.pkl', 'rb'))
      Y_predict = model.predict(X)
      return jsonify({'Prediction': float(Y_predict)})

if __name__ == '__main__':
    app.run(debug=True, port=1010)