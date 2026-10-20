import numpy as np, matplotlib.pyplot as plt

# 1-D slice of groundwater contamination (steady-state diffusion)
# Boundary: left = 100 ppm (spill), right = 0 ppm (clean)
n = 20
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 2
    if i > 0:     A[i, i-1] = -1
    if i < n-1:   A[i, i+1] = -1
b = np.zeros(n); b[0] = 100.0

def gauss_seidel(A, b, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b); errs=[]
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i,:i]@x[:i] - A[i,i+1:]@old[i+1:]) / A[i,i]
        e = np.linalg.norm(x-old, ord=np.inf); errs.append(e)
        if e < tol: break
    return x, errs

x, errs = gauss_seidel(A, b)
exact = np.linalg.solve(A, b)
print("Converged in", len(errs), "iterations")
print("Max error vs exact:", np.max(np.abs(x - exact)))

plt.semilogy(errs)
plt.xlabel("Iteration"); plt.ylabel("Max change")
plt.title("Groundwater diffusion — GS convergence"); plt.grid(True)
plt.savefig("../outputs/Task_08_groundwater.png")
plt.show()