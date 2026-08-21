---
layout: default
title: Addition
parent: Fluids
nav_order: 1
---

# Navier-Stokes Simulation

<p>Add 1 to 1</p>

<input type="number" id="viscosity" value="1.0" style="width: 60px;">
<button onclick="runFluidSim()">Run Fluid Sim</button>
<p><strong>Result:</strong> <span id="result">Ready</span></p>

<script>
async function runFluidSim() {
    let visc = document.getElementById("viscosity").value;
    let url = "https://new-koahla-physics-sims.onrender.com/simulate"; 
    
    let res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ viscosity: visc })
    });
    
    let data = await res.json();
    document.getElementById("result").innerText = data.result;
}
</script>
