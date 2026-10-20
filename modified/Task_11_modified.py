from scipy.optimize import root_scalar
import numpy as np

# Loan APR with monthly payments
# Loan: 25,000 borrowed; repaid with 60 monthly payments of 480
P = 25000.0; n = 60; pmt = 480.0

def balance(r):
    return pmt * (1 - (1+r)**-n)/r - P if r != 0 else pmt*n - P

def d_balance(r):
    h = 1e-8
    return (balance(r+h) - balance(r-h)) / (2*h)

newton = root_scalar(balance, fprime=d_balance, x0=0.01, method="newton", xtol=1e-12)
secant = root_scalar(balance, x0=0.005, x1=0.02, method="secant", xtol=1e-12)

r_n = newton.root
apr = r_n * 12 * 100
print(f"Monthly rate: {r_n:.8f}")
print(f"APR (nominal): {apr:.4f}%")
print(f"Check balance at solution: {balance(r_n):.6f}")
print(f"Secant solution match: {abs(secant.root-r_n):.2e}")