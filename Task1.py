import pandas as pd

# Load the data
banknifty_data = pd.read_csv('BANKNIFTY_historical_data.csv')
finnifty_data = pd.read_csv('FINNIFTY_historical_data.csv')
nifty_data = pd.read_csv('NIFTY_historical_data.csv')

# Display the first few rows of each data set to check
print(banknifty_data.head())
print(finnifty_data.head())
print(nifty_data.head())

from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the data
banknifty_data = pd.read_csv('BANKNIFTY_historical_data.csv')
finnifty_data = pd.read_csv('FINNIFTY_historical_data.csv')
nifty_data = pd.read_csv('NIFTY_historical_data.csv')

@app.route('/get_data', methods=['GET'])
def get_data():
    script = request.args.get('script').upper()
    
    if script == 'BANKNIFTY':
        return jsonify(banknifty_data.to_dict(orient='records'))
    elif script == 'FINNIFTY':
        return jsonify(finnifty_data.to_dict(orient='records'))
    elif script == 'NIFTY':
        return jsonify(nifty_data.to_dict(orient='records'))
    else:
        return jsonify({"error": "Invalid script name"}), 400

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/get_data?script=BANKNIFTY
