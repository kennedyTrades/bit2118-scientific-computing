import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Missing GPS points on a road
t_known = np.array([0, 2, 4, 6, 8, 10], dtype=float)
lat = np.array([-1.2860, -1.2855, -1.2848, -1.2843, -1.2839, -1.2834])

linear = interp1d(t_known, lat, kind="linear")
cubic  = CubicSpline(t_known, lat)

t_missing = 5.0
print(f"Linear estimate at t=5 s : {float(linear(t_missing)):.6f}")
print(f"Cubic  estimate at t=5 s : {float(cubic(t_missing)):.6f}")

tt = np.linspace(0, 10, 200)
plt.scatter(t_known, lat, label="Known GPS", color="black")
plt.plot(tt, linear(tt), label="Linear", linestyle="--")
plt.plot(tt, cubic(tt),  label="Cubic")
plt.xlabel("Time (s)"); plt.ylabel("Latitude (°)")
plt.title("GPS gap filling"); plt.legend(); plt.grid(True)
plt.savefig("../outputs/Task_13_gps.png"); plt.show()