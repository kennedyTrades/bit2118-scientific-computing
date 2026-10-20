import numpy as np
from scipy.integrate import simpson

# OBD-II fuel consumption from flow data (L/h)
t_min  = np.arange(0, 61, 1, dtype=float)
flow_Lh = np.array([
    1.2,1.1,1.0,0.9,0.8,0.7,0.8,1.0,1.3,1.6,
    2.0,2.3,2.4,2.2,2.0,1.8,1.5,1.2,1.0,0.9,
    0.8,0.7,0.6,0.6,0.7,0.9,1.2,1.5,1.8,2.1,
    2.4,2.6,2.7,2.6,2.4,2.1,1.8,1.5,1.3,1.1,
    0.9,0.8,0.7,0.6,0.6,0.7,0.9,1.1,1.3,1.5,
    1.7,1.9,2.0,2.1,2.0,1.9,1.7,1.5,1.3,1.1,1.0], float)

L_trap = np.trapezoid(flow_Lh, t_min/60.0)      # hours
L_simp = simpson(flow_Lh, x=t_min/60.0)

print(f"Fuel used (trapezoid): {L_trap:.3f} L")
print(f"Fuel used (Simpson):   {L_simp:.3f} L")
print(f"Difference: {abs(L_trap - L_simp):.3f} L")