---
layout: default
title: Gravity Simulation
---
# Heavy Simulation

<input type="number" id="num1" value="5">
<button onclick="calculate()">Run Server Simulation</button>
<p>Result: <span id="result">Waiting...</span></p>

<script>
async function calculate() {
    document.getElementById("result").innerText = "Calculating on server (10s)...";
    let n1 = document.getElementById("num1").value;
    
    // Swap this with your Render or PythonAnywhere URL
    let url = "https://your-app-url.com/simulate"; 
    
    let res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ x: n1 })
    });
    
    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}
</script>
