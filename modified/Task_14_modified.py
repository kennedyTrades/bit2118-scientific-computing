import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Crop yield vs rainfall
rain_mm = np.array([50, 100, 150, 200, 250, 300, 350, 400], float)
yield_t = np.array([1.2, 2.5, 3.4, 4.0, 4.1, 3.7, 3.0, 2.1])

def model(x, a, b, c): return a*x**2 + b*x + c

p, _ = curve_fit(model, rain_mm, yield_t)
pred = model(rain_mm, *p)
rmse = np.sqrt(np.mean((yield_t - pred)**2))
peak_x = -p[1]/(2*p[0])

print(f"y = {p[0]:.5f}x^2 + {p[1]:.4f}x + {p[2]:.3f}")
print(f"RMSE: {rmse:.4f} t/ha")
print(f"Optimal rainfall (peak): {peak_x:.1f} mm -> yield {model(peak_x,*p):.2f} t/ha")

xs = np.linspace(50, 400, 300)
plt.scatter(rain_mm, yield_t, label="Observed", color="black")
plt.plot(xs, model(xs, *p), label="Fitted", color="green")
plt.xlabel("Rain (mm)"); plt.ylabel("Yield (t/ha)")
plt.title("Crop yield vs rainfall"); plt.legend(); plt.grid(True)
plt.savefig("../outputs/Task_14_crop.png"); plt.show()