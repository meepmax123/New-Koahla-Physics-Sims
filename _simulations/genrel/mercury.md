---
layout: default
title: Mercury Precession
parent: General Relativity
nav_order: 1
---

# Mercury Orbital Precession due to General Relativistic Correction Simulation

<p>This simulation runs?</p>

<input type="number" id="scalar" value="1.0" style="width: 60px;">
<button onclick="runSim()">Run Mercury Sim</button>
<p><strong>Result:</strong> <span id="result">Ready</span></p>

<script>
async function runSim() {
    document.getElementById("result").innerText = "Running";
    let visc = document.getElementById("scalar").value;
    let url = "https://new-koahla-physics-sims.onrender.com/simulations/fluids"; 
    
    let res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ viscosity: visc })
    });
    
    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}
</script>
