import numpy as np

def run_fluid_simulation(data):
    """
    Handles math and processing for the fluid simulation.
    Expects a dictionary containing input parameters.
    """
    viscosity = float(data.get('viscosity', 1.0))

    # 1D Viscous Fluid Diffusion Calculation
    nodes = 50
    u = np.sin(np.linspace(0, np.pi, nodes))
    dt, dx = 0.001, 0.05

    for _ in range(500):
        u[1:-1] += viscosity * dt / (dx**2) * (u[2:] - 2*u[1:-1] + u[:-1])

    max_vel = float(np.max(u))
    avg_vel = float(np.mean(u))

    return {
        "result": f"Peak Velocity: {max_vel:.4f} m/s | Avg Velocity: {avg_vel:.4f} m/s"
    }
