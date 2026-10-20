import numpy as np, matplotlib.pyplot as plt

# Drug concentration in bloodstream (first-order elimination)
# dC/dt = -k*C
C0 = 5.0       # mg/L initial
k  = 0.15      # per hour
h  = 0.25      # hours
T_end = 24.0

t = np.arange(0, T_end+h, h)
C = np.zeros_like(t); C[0] = C0
for i in range(len(t)-1):
    C[i+1] = C[i] + h * (-k * C[i])

exact = C0 * np.exp(-k*t)
print(f"Euler C(12h): {C[int(12/h)]:.4f} mg/L")
print(f"Exact C(12h): {exact[int(12/h)]:.4f} mg/L")
print(f"Final absolute error: {abs(C[-1]-exact[-1]):.4f} mg/L")

plt.plot(t, C, "o-", label="Euler")
plt.plot(t, exact, label="Exact", linestyle="--")
plt.xlabel("Time (h)"); plt.ylabel("Concentration (mg/L)")
plt.title("Drug elimination (Euler)"); plt.legend(); plt.grid(True)
plt.savefig("../outputs/Task_17_drug.png"); plt.show()