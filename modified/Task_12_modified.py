import numpy as np
from scipy.optimize import root

# Robot arm reach vs obstacle (circle vs line)
# Circle: x^2 + y^2 = 4 (reach radius 2)
# Line: y = 0.5x + 0.3 (obstacle wall)
def eqs(z):
    x, y = z
    return [x**2 + y**2 - 4,      
            y - (0.5*x + 0.3)]    

for guess in ([1.5, 1.0], [-1.8, -0.6]):
    s = root(eqs, guess)
    print("guess", guess, "->", s.x, "residual", eqs(s.x), "ok", s.success)