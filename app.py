from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

# --- SIMULATION 1: Fluid Dynamics ---
@app.route('/simulations/fluid', methods=['POST'])
def fluid_sim():
    data = request.json or {}
    viscosity = float(data.get('viscosity', 1.0))
    
    # Fluid physics math...
    result_value = viscosity * 9.81  # Example calculation
    
    return jsonify({"result": f"Fluid Flow Speed: {result_value:.2f} m/s"})


# --- SIMULATION 2: Double Pendulum ---
@app.route('/simulations/pendulum', methods=['POST'])
def pendulum_sim():
    data = request.json or {}
    length = float(data.get('length', 1.0))
    angle = float(data.get('angle', 45.0))
    
    # Chaos/Pendulum physics math...
    period = 2 * np.pi * np.sqrt(length / 9.81)
    
    return jsonify({"result": f"Oscillation Period: {period:.2f} seconds"})


# --- SIMULATION 3: Orbital Mechanics ---
@app.route('/simulations/orbit', methods=['POST'])
def orbit_sim():
    data = request.json or {}
    mass = float(data.get('mass', 5.97e24)) # Earth mass default
    altitude = float(data.get('altitude', 400000)) # 400 km
    
    # Orbital velocity math...
    G = 6.674e-11
    R = 6371000 + altitude
    v = np.sqrt(G * mass / R)
    
    return jsonify({"result": f"Required Orbital Speed: {v:.2f} m/s"})

if __name__ == "__main__":
    app.run()
