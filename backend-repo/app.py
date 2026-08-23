from flask import Flask, request, jsonify
from flask_cors import CORS

# Import the specific function from physics/fluid.py
from physics.fluid import run_fluid_simulation
from physics.mercurygenrel import run_mercurygenrel_simulation

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/simulations/genrel/mercury', methods=['POST'])
def mercurygenrel_sim():
    data = request.json or {}
    
    # Run simulation logic from external file
    #simulation_result = run_mercurygenrel_simulation(data)
    
    return jsonify(run_mercurygenrel_simulation(data))
@app.route('/simulations/fluids/test', methods=['POST'])
def fluid_sim():
    data = request.json or {}
    
    # Run simulation logic from external file
    #simulation_result = run_fluid_simulation(data)
    
    return jsonify(run_fluid_simulation(data))


if __name__ == "__main__":
    app.run()
