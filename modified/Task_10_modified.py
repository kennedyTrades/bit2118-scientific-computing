from scipy.optimize import root_scalar
import numpy as np, matplotlib.pyplot as plt

# Break-even point for a small business
def profit(x):
    return (25*x - 0.02*x**2) - (500 + 8*x)

sol = root_scalar(profit, bracket=[0, 100], method="bisect", xtol=1e-10)
print(f"Break-even units: {sol.root:.2f}")

xs = np.linspace(0, 100, 300)
plt.plot(xs, profit(xs)); plt.axhline(0, lw=.8, color='black')
plt.axvline(sol.root, ls="--", color='red')
plt.xlabel("Units sold"); plt.ylabel("Profit")
plt.title("Break-even analysis"); plt.grid(True)
plt.savefig("../outputs/Task_10_breakeven.png"); plt.show()