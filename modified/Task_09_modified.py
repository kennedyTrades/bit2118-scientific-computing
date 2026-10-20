import numpy as np

# 6-person social group; weighted friendships (0=no tie, 1=friend)
A = np.array([
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
], dtype=float)

vals, vecs = np.linalg.eig(A)
idx = np.argmax(np.real(vals))
lam = np.real(vals[idx])
v   = np.abs(np.real(vecs[:, idx]))
centrality = v / v.sum()

names = ["Alice","Bob","Carol","Dave","Eve","Frank"]
for n, c in zip(names, centrality):
    print(f"{n:6s}: {c:.4f}")

print("Dominant eigenvalue:", lam)
print("Verification error ||Av - λv||:", np.linalg.norm(A@v - lam*v))