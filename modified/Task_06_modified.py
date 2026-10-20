import numpy as np

# Fuel blending for a target octane
# Blend fuel A (octane 91) and B (octane 98) + ethanol C (octane 109)
# Constraints: total volume 1000 L, octane target 95, ethanol 10% (100 L)
# Unknowns: x = litres A, y = litres B, z = litres C

A = np.array([
    [1.0,   1.0,   1.0],     # total volume
    [91.0,  98.0,  109.0],   # weighted octane
    [0.0,   0.0,   1.0],     # ethanol fixed at 100 L
])
b = np.array([1000.0, 95.0*1000.0, 100.0])

sol = np.linalg.solve(A, b)
residual = b - A @ sol

print(f"Fuel A: {sol[0]:.2f} L")
print(f"Fuel B: {sol[1]:.2f} L")
print(f"Ethanol C: {sol[2]:.2f} L")
print("Residual norm:", np.linalg.norm(residual))