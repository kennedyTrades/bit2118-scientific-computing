import numpy as np

# Hourly fridge readings (°C) — pharmacy cold chain
fridge_c = np.array([4.1, 4.0, 3.8, 3.9, 4.2, 5.0, 6.1, 7.2,
                     8.4, 9.1, 8.7, 7.5, 6.8, 6.0, 5.5, 5.1,
                     4.9, 4.6, 4.4, 4.3, 4.2, 4.1, 4.0, 4.0])

mean_t = np.mean(fridge_c)
min_t  = np.min(fridge_c)
max_t  = np.max(fridge_c)
fridge_f = 1.8 * fridge_c + 32

risk_hours = np.where(fridge_c > 8.0)[0]
risk_vals  = fridge_c[risk_hours]

print(f"Mean fridge temp: {mean_t:.2f} C")
print(f"Min / Max: {min_t:.1f} / {max_t:.1f} C")
print(f"First six Fahrenheit: {fridge_f[:6]}")
print(f"Hours above 8 C: {risk_hours.tolist()} -> {risk_vals}")
print("Spoilage-risk flag:", "YES" if risk_vals.size else "NO")