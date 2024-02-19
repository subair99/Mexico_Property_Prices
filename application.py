# Import required modules
import pickle
import gzip
from flask import Flask, request, app, render_template
import pandas as pd

# Define application.
application = Flask(__name__)
app = application

# Load the model and preocessor
loaded_model = pickle.load(gzip.open('mexico_model.pkl', 'rb'))

# Specify app route for Home
@app.route('/')
def home():
    return render_template('home.html')

# Specify app route for predict
@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == 'GET':
        return render_template('index.html')
    
    else:

        '''
        For rendering results on HTML GUI
        '''
        # Retrive values from form
        values = [x for x in request.form.values()]

        # Define raw data
        raw_data = {
            'property_type': values[0],
            'borough': values[1],
            'surface_covered_in_m2': values[2],
            'price_per_m2': values[3],
            'lat': values[4],
            'lon': values[5]
        }
        
        # Create function to predict the raw data
        def predict_data(raw_data):
            data_frame = pd.DataFrame(raw_data, index=[0])
            data_predict = loaded_model.predict(data_frame)
            return data_predict[0]
        
        # Perform prediction
        prediction = predict_data(raw_data)

        return render_template('home.html', prediction_result=
                               f'The Price of the {raw_data["property_type"]} is: ${prediction:.2f}')




if __name__=="__main__":
    app.run(host="0.0.0.0")