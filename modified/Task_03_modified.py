import numpy as np
import timeit

rng = np.random.default_rng(7)
# Simulated ECG samples in millivolts (10 s at 500 Hz = 5000 samples)
ecg_mv = rng.normal(0.0, 0.8, 5000) + np.sin(np.linspace(0, 20*np.pi, 5000))

def loop_energy():
    out = []
    for v in ecg_mv:
        out.append((v/1000.0)**2)   # mV -> V, then square
    return out

def vec_energy():
    return (ecg_mv/1000.0)**2

t_loop = timeit.timeit(loop_energy, number=1)
t_vec  = timeit.timeit(vec_energy,  number=3)/3

e = vec_energy()
print("First five energy samples:", e[:5])
print(f"Total signal energy (V^2 samples): {e.sum():.6f}")
print(f"Loop time: {t_loop:.4f}s | Vectorised: {t_vec:.6f}s")
print(f"Speed-up: {t_loop/t_vec:.1f}x")