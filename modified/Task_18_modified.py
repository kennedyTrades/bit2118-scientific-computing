import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Drug concentration with absorption (two-compartment)
# dG/dt = -ka*G ;  dP/dt = ka*G - ke*P
ka = 0.8   # absorption /h
ke = 0.15  # elimination /h
dose = 100.0  # mg

def pk(t, y):
    G, P = y
    return [-ka*G, ka*G - ke*P]

sol = solve_ivp(pk, (0, 24), [dose, 0.0], t_eval=np.linspace(0, 24, 400), rtol=1e-9, atol=1e-11)

P = sol.y[1]
t_peak = sol.t[np.argmax(P)]
print("Solver success:", sol.success)
print(f"Peak plasma concentration: {P.max():.3f} mg at t={t_peak:.2f} h")
print(f"Concentration at 24 h: {P[-1]:.4f} mg")

plt.plot(sol.t, sol.y[0], label="Gut (G)")
plt.plot(sol.t, P,        label="Plasma (P)")
plt.xlabel("Time (h)"); plt.ylabel("Amount (mg)")
plt.title("Oral drug pharmacokinetics"); plt.legend(); plt.grid(True)
plt.savefig("../outputs/Task_18_pk.png"); plt.show()