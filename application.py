<<<<<<< HEAD
# Import required modules.
import pickle
=======
# Import required modules
import pickle
import gzip
>>>>>>> 2cd3cceea58a166043e1bc9a6372945d2aeeb871
from flask import Flask, request, app, render_template
import pandas as pd

# Define application.
application = Flask(__name__)
app = application

<<<<<<< HEAD
# Load the model
loaded_model = pickle.load(open('renewable_energy_model.pkl', 'rb'))
=======
# Load the model and preocessor
loaded_model = pickle.load(gzip.open('mexico_model.pkl', 'rb'))
>>>>>>> 2cd3cceea58a166043e1bc9a6372945d2aeeb871

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
<<<<<<< HEAD

=======
>>>>>>> 2cd3cceea58a166043e1bc9a6372945d2aeeb871
        # Retrive values from form
        values = [x for x in request.form.values()]

        # Define raw data
        raw_data = {
<<<<<<< HEAD
            'property_type': values[0],
            'borough': values[1],
            'surface_covered_in_m2': values[2],
            'price_per_m2': values[3],
            'lat': values[4],
            'lon': values[5]
        }
=======
<<<<<<< HEAD
                    'Traffic_Conditions': values[0],
                    'Number_of_Packages': values[1],
                    'Distance_(miles)': values[2],
                    'fog': values[3],
                    'rain': values[4],
                    'snow': values[5],
                    'hail': values[6],
                    'month_of_delvery': values[7]
=======
                    'property_type': values[0],
                    'borough': values[1],
                    'surface_covered_in_m2': values[2],
                    'price_per_m2': values[3],
                    'lat': values[4],
                    'lon': values[5]
>>>>>>> 2cd3cceea58a166043e1bc9a6372945d2aeeb871
                    }
>>>>>>> b82deead7c273dd2709591a890ca46d509470c89
        
        # Create function to predict the raw data
        def predict_data(raw_data):
            data_frame = pd.DataFrame(raw_data, index=[0])
            data_predict = loaded_model.predict(data_frame)
            return data_predict[0]
        
        # Perform prediction
        prediction = predict_data(raw_data)

<<<<<<< HEAD
        return render_template('home.html', prediction_result=
                               f'The Price of the {raw_data["property_type"]} is: ${prediction:.2f}')
=======
<<<<<<< HEAD
        return render_template('home.html', prediction_result=f'Historical Delivery Time is: {prediction} Hours')
=======
        return render_template('home.html', prediction_result=f'The Price of the {raw_data["property_type"]} is: ${prediction}')
>>>>>>> b82deead7c273dd2709591a890ca46d509470c89


>>>>>>> 2cd3cceea58a166043e1bc9a6372945d2aeeb871


if __name__=="__main__":
    app.run(host="0.0.0.0")