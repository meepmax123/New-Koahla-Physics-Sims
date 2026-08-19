# Testing Python Code

<p>This page uses WebAssembly to run Python directly inside your browser.</p>

<!-- Inputs for the numbers -->
<input type="number" id="num1" value="5" style="width: 60px;"> + 
<input type="number" id="num2" value="10" style="width: 60px;">

<!-- Click Trigger -->
<button onclick="calculate()" id="btn" style="margin-left: 10px;">Add Numbers</button>

<!-- Result Output Area -->
<p><strong>Result:</strong> <span id="result">Loading Python Engine...</span></p>

<!-- Load the Pyodide WebAssembly Script Engine -->
<script src="https://jsdelivr.net"></script>

<script>
    let pyodide;
    let isReady = false;

    // 1. Initialize the Python environment when page loads
    async function loadEngine() {
        pyodide = await loadPyodide();
        document.getElementById("result").innerText = "Ready!";
        isReady = true;
    }
    loadEngine();

    // 2. This function runs when you click the button
    async function calculate() {
        if (!isReady) return;

        // Grab values from the HTML inputs
        let n1 = document.getElementById("num1").value;
        let n2 = document.getElementById("num2").value;

        // Pass JavaScript values into Python variables
        pyodide.globals.set("x", parseFloat(n1));
        pyodide.globals.set("y", parseFloat(n2));

        // Execute the Python code block
        let pythonCode = `
result = x + y
f"{x} + {y} equals {result}"
        `;

        // Send the output back to the webpage
        let output = await pyodide.runPythonAsync(pythonCode);
        document.getElementById("result").innerText = output;
    }
</script>
