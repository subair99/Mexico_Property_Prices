# Import required modules.
import pickle
from flask import Flask, request, app, render_template
import pandas as pd

# Define application.
application = Flask(__name__)
app = application

# Load the model
loaded_model = pickle.load(open('renewable_energy_model.pkl', 'rb'))

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
                    'Traffic_Conditions': values[0],
                    'Number_of_Packages': values[1],
                    'Distance_(miles)': values[2],
                    'fog': values[3],
                    'rain': values[4],
                    'snow': values[5],
                    'hail': values[6],
                    'month_of_delvery': values[7]
                    }
        
        # Create function to predict the raw data
        def predict_data(raw_data):
            data_frame = pd.DataFrame(raw_data, index=[0])
            data_predict = loaded_model.predict(data_frame)
            return data_predict[0]
        
        # Perform prediction
        prediction = predict_data(raw_data).round(2)

        return render_template('home.html', prediction_result=f'Historical Delivery Time is: {prediction} Hours')


if __name__=="__main__":
    app.run(host="0.0.0.0")