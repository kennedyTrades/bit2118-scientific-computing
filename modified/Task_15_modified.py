import numpy as np, matplotlib.pyplot as plt

# Heart-rate change from a wearable
t = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16], float)   # minutes
hr = np.array([62, 68, 78, 92, 110, 128, 140, 145, 142]) # bpm

hr_rate = np.zeros_like(hr)
hr_rate[0]  = (hr[1] - hr[0]) / (t[1] - t[0])
hr_rate[-1] = (hr[-1] - hr[-2]) / (t[-1] - t[-2])
for i in range(1, len(t)-1):
    hr_rate[i] = (hr[i+1] - hr[i-1]) / (t[i+1] - t[i-1])

for ti, h, r in zip(t, hr, hr_rate):
    print(f"t={ti:>4.0f} min  HR={h:>4} bpm  dHR/dt={r:+.2f} bpm/min")

plt.plot(t, hr_rate, marker="o")
plt.xlabel("Time (min)"); plt.ylabel("dHR/dt (bpm/min)")
plt.title("Heart-rate response during exercise"); plt.grid(True)
plt.savefig("../outputs/Task_15_hr.png"); plt.show()