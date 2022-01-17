import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model

model = pickle.load(open('model_pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]

    # Convert features to array
    array_features = [np.array(features)]

    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 'Light':
        return render_template('light.html', result = 'Light Rain')
    elif output == 'None':
        return render_template('none.html', result = 'None')
    elif output == 'Medium':
        return render_template('medium.html', result = 'Medium Rain')
    elif output == 'Heavy and Above':
        return render_template('heavy.html', result = 'Heavy and Above Rain')
    else:
        return render_template('predict.html', result = 'Unpredictable')

if __name__ == '__main__':
#Run the application
    app.run()
    
    