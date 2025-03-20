from flask import Flask, request, jsonify  # Importing Flask modules
import util  # Importing util.py functions

app = Flask(__name__)  # Initializing the Flask app

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()  # Calls the function from util.py
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow frontend access

    return response

@app.route('/predict_house_price', methods=['GET', 'POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow frontend access

    return response

if __name__ == "__main__":
    print("Starting Server...")
    util.load_saved_artifacts()  # Loads ML model and artifacts from util.py
    app.run()  # Runs the server
