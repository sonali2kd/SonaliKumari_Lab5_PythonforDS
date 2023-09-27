from flask import Flask, request, jsonify , render_template
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['GET'])
def Homepage():
    return render_template('index.html')
@app.route('/predict', methods =['POST'])
def predict():
    if request.method== 'POST':
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type = request.form['Fuel_Type']
        Age_of_the_car = request.form['Age_of_the_car']
        Seller_Type = request.form['Seller_Type']
        Transmission = request.form['Transmission']

        prediction = model.predict([[Present_Price, Kms_Driven, Owner, Fuel_Type, Age_of_the_car, Seller_Type, Transmission]])
        output = round(prediction[0],2)
        return render_template('index.html', prediction_text = "You can sell your car at {} lakhs".format(output))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
