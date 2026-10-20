import numpy as np
from scipy.linalg import lu_factor, lu_solve
import time

# 5-node network admittance-style matrix (fixed)
A = np.array([
    [ 4., -1.,  0.,  0.,  0.],
    [-1.,  4., -1.,  0.,  0.],
    [ 0., -1.,  4., -1.,  0.],
    [ 0.,  0., -1.,  4., -1.],
    [ 0.,  0.,  0., -1.,  3.],
])

# Daily demand vectors for 7 days
daily_loads = [np.array([10., 12., 14., 16., 12.]),
               np.array([11., 13., 15., 17., 13.]),
               np.array([ 9., 11., 13., 15., 11.]),
               np.array([12., 14., 16., 18., 14.]),
               np.array([13., 15., 17., 19., 15.]),
               np.array([10., 11., 12., 13., 11.]),
               np.array([ 8., 10., 12., 14., 10.])]

lu, piv = lu_factor(A)          # factor once
t0 = time.perf_counter()
for day, b in enumerate(daily_loads, 1):
    x = lu_solve((lu, piv), b)
    print(f"Day {day}: loads = {x.round(4)}  residual={np.linalg.norm(b - A@x):.1e}")
t_lu = time.perf_counter() - t0

# Compare with refactoring each day
t0 = time.perf_counter()
for b in daily_loads:
    np.linalg.solve(A, b)
t_direct = time.perf_counter() - t0

print(f"LU reuse time: {t_lu:.6f}s | Direct solve each day: {t_direct:.6f}s")