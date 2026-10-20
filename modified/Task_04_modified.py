import numpy as np

# Bank interest over 10,000 compounding steps
principal = 1000.0
rate = 0.05 / 365      # 5% annual, daily compounding
days = 10000

# Unstable: repeated multiplication accumulates round-off
balance_unstable = principal
for _ in range(days):
    balance_unstable *= (1 + rate)

# Stable: closed-form compound interest
balance_stable = principal * (1 + rate) ** days

print(f"Step-by-step balance : {balance_unstable:.10f}")
print(f"Closed-form balance  : {balance_stable:.10f}")
print(f"Absolute error vs closed-form: {abs(balance_unstable - balance_stable):.3e}")
print(f"Relative error: {abs(balance_unstable - balance_stable)/balance_stable:.3e}")