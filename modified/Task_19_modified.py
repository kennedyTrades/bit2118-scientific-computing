import numpy as np
from scipy.optimize import minimize

# Delivery-route fuel minimisation
# Truck A: 16 L/trip, 5 t. Truck B: 24 L/trip, 8 t. Need 120 t.
def fuel(z):
    x, y = z
    return 16*x + 24*y

def demand(z):
    x, y = z
    return 5*x + 8*y - 120

sol = minimize(fuel, x0=[10, 10], method="SLSQP", bounds=[(0, None), (0, None)], constraints=[{"type": "ineq", "fun": demand}])

print("success:", sol.success)
print(f"Truck A trips: {sol.x[0]:.2f}")
print(f"Truck B trips: {sol.x[1]:.2f}")
print(f"Total fuel: {sol.fun:.2f} L -> ${sol.fun*1.6:.2f}")

best = None
for a in range(0, 30):
    for b in range(0, 30):
        if 5*a + 8*b >= 120:
            cost = 16*a + 24*b
            if best is None or cost < best[0]:
                best = (cost, a, b)
print("Best integer plan:", best)