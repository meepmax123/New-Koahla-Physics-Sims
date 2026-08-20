from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app) # Vital: Allows GitHub Pages to communicate with this server

@app.route('/simulate', methods=['POST'])
def sim():
    data = request.json
    x = float(data.get('x', 0))
    
    time.sleep(10) # Your actual physics math goes here
    
    return jsonify({"result": f"Simulation Complete: {x + 9.81}"})
