---
layout: page
title: Projectile Simulation
---
# Test simulation
This simulation was written by Gemini to test the implementation of python code in this website.
All future python simulations will be written without AI and this one will be deleted.
A similar experiment will be performed with the C/C++ simulations.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- 1. Load the Pyodide WebAssembly script engine -->
    <script src="https://jsdelivr.net"></script>
</head>
<body>

    <h2>Interactive Physics Simulator</h2>
    <p>Adjust variables and run the Python engine below.</p>

    <!-- 2. Create input fields for user parameters -->
    <div style="margin-bottom: 15px;">
        <label for="velocity">Initial Velocity (m/s): </label>
        <input type="number" id="velocity" value="25" min="1" max="100">
    </div>

    <div style="margin-bottom: 15px;">
        <label for="angle">Launch Angle (degrees): </label>
        <input type="number" id="angle" value="45" min="0" max="90">
    </div>

    <!-- 3. The Trigger Button -->
    <button onclick="runSimulation()" id="run-btn">Run Python Simulation</button>

    <!-- 4. Output Display Area -->
    <h3>Results:</h3>
    <pre id="output">Loading Python engine, please wait...</pre>

    <script>
        let pyodideReady = false;
        let pyodide;

        // Automatically initialize Python engine when the web page opens
        async function main() {
            pyodide = await loadPyodide();
            document.getElementById("output").innerText = "Python engine ready! Click run.";
            pyodideReady = true;
        }
        main();

        // Function that fires when the user clicks the button
        async function runSimulation() {
            if (!pyodideReady) return;

            // Grab the real-time values from the web inputs
            let v = document.getElementById("velocity").value;
            let a = document.getElementById("angle").value;

            // Clear previous calculations and update button text
            document.getElementById("output").innerText = "Calculating...";

            // Pass variables from Javascript into the Pyodide global environment
            pyodide.globals.set("v0", parseFloat(v));
            pyodide.globals.set("angle_deg", parseFloat(a));

            // Write your pure Python physics script as a multi-line string
            let pythonCode = `
import math

# Acceleration due to gravity
g = 9.81

# Convert degrees to radians for math library
theta = math.radians(angle_deg)

# Physics formulas for standard range and flight time
time_of_flight = (2 * v0 * math.sin(theta)) / g
max_height = (v0**2 * (math.sin(theta))**2) / (2 * g)
range_horizontal = (v0**2 * math.sin(2 * theta)) / g

# Construct a clean string response to send back to the web window
result = f"Time of flight: {time_of_flight:.2f} seconds\\n"
result += f"Max Height reached: {max_height:.2f} meters\\n"
result += f"Total Distance: {range_horizontal:.2f} meters"
result
            `;

            try {
                // Run the Python environment code and grab the final string evaluation
                let pyResult = await pyodide.runPythonAsync(pythonCode);
                document.getElementById("output").innerText = pyResult;
            } catch (err) {
                document.getElementById("output").innerText = "Python Error:\\n" + err;
            }
        }
    </script>
</body>
</html>
