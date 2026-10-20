import numpy as np, matplotlib.pyplot as plt

rng = np.random.default_rng(2024)

# Project-cost risk (PERT simulation)
# Three project phases, each with triangular (min, mode, max) duration in days
phases = [(10, 12, 20), (8, 10, 15), (12, 14, 22)]
N = 200_000
cost_per_day = 5000.0
budget = 250_000.0

# Simulate each phase
durations = np.array([rng.triangular(mn, mode, mx, N) for (mn, mode, mx) in phases])
total_days = durations.sum(axis=0)
total_cost = total_days * cost_per_day
over_budget = (total_cost > budget).mean()

print(f"Estimated mean project days: {total_days.mean():.2f}")
print(f"Estimated mean cost: ${total_cost.mean():,.0f}")
print(f"P(cost > budget): {over_budget:.4%}")

# Convergence plot
idx = np.unique(np.logspace(0, np.log10(N), 200).astype(int) - 1)
running = np.cumsum(total_cost > budget) / np.arange(1, N+1)
plt.semilogx(idx+1, running[idx])
plt.xlabel("Simulations"); plt.ylabel("P(over budget)")
plt.title("Monte Carlo project-cost risk"); plt.grid(True)
plt.savefig("../outputs/Task_20_project_risk.png"); plt.show()