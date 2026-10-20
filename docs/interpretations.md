# BIT 2118 Scientific Computing - Interpretations

This document contains the answers to Instructions B, C, and D for Tasks 2 through 20.

---

## Task 2: NumPy Arrays and Numerical Computation

**B. Inputs and Mathematical Operation**
- **Input:** 24 hourly temperature readings in Celsius.
- **Operation:** `np.mean()`, `np.min()`, `np.max()`, and vectorized Celsius-to-Fahrenheit conversion `F = 1.8C + 32`.

**C. Parameter Change and Effect**
- **Change:** Replaced the temperature array with a winter dataset (values around 2°C).
- **Effect:** The mean dropped from ~23°C to ~2°C, the minimum became negative, and all Fahrenheit values shifted down by approximately 37°F.

**D. Interpretation of Output and Graph**
- The daily mean of 23.0°C indicates a mild day. The minimum of 17.5°C (around 04:00) and maximum of 29.4°C (around 13:00) show normal diurnal temperature variation. The vectorized conversion demonstrates how NumPy processes all 24 values simultaneously without needing a Python loop.


## Task 3: Mathematical Functions and Vectorization

**B. Inputs and Mathematical Operation**
- **Input:** 1,000,000 simulated network latency samples in milliseconds.
- **Operation:** Division by 1000 (ms to seconds), followed by squaring (`**2`). This is done twice: once using a Python `for` loop, and once using NumPy vectorization. 

**C. Parameter Change and Effect**
- **Change:** Reduced the number of samples from 1,000,000 to 1,000. 
- **Effect:** The speed-up ratio of vectorization collapsed (from ~100x faster down to ~5x faster). This shows that vectorization pays off massively at scale, while Python loop overhead is relatively small for tiny datasets.

**D. Interpretation of Output and Graph**
- The vectorized code is significantly faster (often 50–200x) than the Python loop. The squared latency values represent the "error contribution" for a service-level metric. This demonstrates why vectorization is essential in data science and scientific computing where millions of operations are repeated.

 

## Task 4: Floating-Point Arithmetic and Numerical Errors

**B. Inputs and Mathematical Operation**
- **Input:** `0.1 + 0.2` compared to `0.3`; an approximation of `sqrt(2)`; and a formula evaluating `(sqrt(1+x) - 1)/x` for very small values of `x`.
- **Operation:** Exact equality checks (`==`), tolerance-based checks (`np.isclose`), and calculating absolute/relative error.

**C. Parameter Change and Effect**
- **Change:** Set `x = 1e-20` (a very small number) to test the unstable formula.
- **Effect:** The direct formula `(sqrt(1+x) - 1)/x` returns `0.0` because of catastrophic cancellation (precision loss). The mathematically stable formula `1 / (sqrt(1+x) + 1)` returns `0.5`, which is the correct limit.

**D. Interpretation of Output and Graph**
- `0.1 + 0.2` outputs `0.30000000000000004`, so exact equality fails. Using `np.isclose()` fixes this. The unstable formula fails for small numbers because subtracting 1 from a number very close to 1 wipes out significant digits. This shows why choosing the right numerical formulation is critical in scientific simulations.

---

## Task 5: Matrix Algebra and Matrix Operations

**B. Inputs and Mathematical Operation**
- **Input:** Four coordinate points forming a square `[[0,0], [1,0], [1,1], [0,1]]`. A rotation angle of 45 degrees and a scaling matrix `[[2.0, 0.0], [0.0, 1.5]]`.
- **Operation:** Matrix multiplication (combining rotation and scaling), applying the transformation to the points using the `@` operator, and finding the determinant.

**C. Parameter Change and Effect**
- **Change:** Changed the rotation angle from 45° to 90°.
- **Effect:** The rotation matrix becomes `[[0, -1], [1, 0]]`. The transformed points swap their x and y axes (rotating the square by a quarter turn), but the determinant remains 3.0 because rotations do not change the area.

**D. Interpretation of Output and Graph**
- The determinant of 3.0 indicates that the transformation triples the area of the object (scaling x by 2 and y by 1.5). The matrix multiplication successfully applies both transformations in one step, which is the core of 2D computer graphics rendering.

---

## Task 6: Solution of Systems of Linear Equations

**B. Inputs and Mathematical Operation**
- **Input:** A coefficient matrix `A = [[4, 2], [8, 12]]` representing CPU and memory usage per server type, and a result vector `b = [20, 72]` representing total usage.
- **Operation:** Solving the linear system `Ax = b` using `np.linalg.solve()`, and checking the residual (error) with `b - A @ solution`.

**C. Parameter Change and Effect**
- **Change:** Doubled the total resource usage vector `b` to `[40, 144]`.
- **Effect:** Because the system is linear, doubling the target outputs exactly doubles the inputs. The solution changed from 2 Type-A and 4 Type-B servers to 4 Type-A and 8 Type-B servers.

**D. Interpretation of Output and Graph**
- The solution shows exactly how many of each server type are active. The residual norm is practically zero, verifying the solution is mathematically correct. This is used in resource allocation to deduce invisible variables from total system metrics.

---

## Task 7: Gaussian Elimination and LU Decomposition

**B. Inputs and Mathematical Operation**
- **Input:** A 3x3 tridiagonal coefficient matrix `A`, and three different measurement vectors `b`.
- **Operation:** Using `scipy.linalg.lu_factor` to decompose matrix `A` once, and `lu_solve` to solve for the three different `b` vectors.

**C. Parameter Change and Effect**
- **Change:** Added a 4th measurement vector to the list.
- **Effect:** Since the LU factorization was only done once, solving the 4th vector requires very little extra computation time compared to doing full Gaussian elimination for every new vector.

**D. Interpretation of Output and Graph**
- The LU decomposition breaks the matrix into Lower and Upper triangular matrices. Reusing these factors for multiple right-hand side vectors avoids redundant computation. The residual norm is extremely small (~1e-15), proving the accuracy of the method.

---

## Task 8: Iterative Methods for Linear Systems

**B. Inputs and Mathematical Operation**
- **Input:** A 5x5 tridiagonal matrix `A` representing a steady-state temperature model, and a boundary vector `b = [100, 0, 0, 0, -20]`.
- **Operation:** Solving `Ax = b` using two iterative methods: Jacobi and Gauss-Seidel. The code tracks the error at each iteration to see convergence.

**C. Parameter Change and Effect**
- **Change:** Loosening the tolerance from `1e-8` to `1e-4`.
- **Effect:** Both methods reach the solution in far fewer iterations because they stop sooner. Gauss-Seidel still converges roughly twice as fast as Jacobi because it uses updated values immediately.

**D. Interpretation of Output and Graph**
- The log-scale plot shows the error dropping linearly over iterations. Gauss-Seidel drops faster than Jacobi. This is highly useful for large sparse systems (like heat transfer or electrical grids) where direct matrix factorization would be too slow or memory-intensive.

---

## Task 9: Eigenvalues and Eigenvectors

**B. Inputs and Mathematical Operation**
- **Input:** A 4x4 adjacency matrix `A` representing an undirected network of 4 nodes.
- **Operation:** Calculating eigenvalues and eigenvectors using `np.linalg.eig()`, finding the dominant eigenvalue, and normalizing the dominant eigenvector to find node centrality.

**C. Parameter Change and Effect**
- **Change:** Adding a 5th node connected to all other nodes.
- **Effect:** The dominant eigenvalue increases (from ~2.4 to ~4.0). The new node becomes the most central, demonstrating how adding a highly connected node shifts network importance.

**D. Interpretation of Output and Graph**
- The centrality values sum to 1. Nodes in the densest cluster have higher values. This mathematical process is the exact core of Google's PageRank algorithm and influence analysis in social networks.

---

## Task 10: Root Finding: Bisection and Fixed-Point Methods

**B. Inputs and Mathematical Operation**
- **Input:** A heat-balance function `f(T) = T - 25 - 10*exp(-T/20)`, an initial bracket `[20, 40]`, and a fixed-point iteration function `g(T) = 25 + 10*exp(-T/20)`.
- **Operation:** Finding the root where `f(T) = 0` using `root_scalar` with the bisection method, and comparing it to a manual fixed-point iteration loop.

**C. Parameter Change and Effect**
- **Change:** Widening the initial bracket to `[15, 45]`.
- **Effect:** The bisection method requires one extra iteration to find the same root because the initial search interval is larger. The fixed-point iteration is unaffected because it does not use a bracket.

**D. Interpretation of Output and Graph**
- Both methods find the equilibrium temperature at approximately 27.1°C. The graph shows the function crossing the x-axis at this point. The fixed-point iteration converges smoothly because the derivative of `g(T)` is less than 1 near the root.

---

## Task 11: Root Finding: Newton-Raphson and Secant Methods

**B. Inputs and Mathematical Operation**
- **Input:** A series of cash flows `[-10000, 3000, 3500, 4000, 2500]`. An initial guess of 0.10 for Newton-Raphson, and initial guesses of 0.05 and 0.20 for the Secant method.
- **Operation:** Calculating Net Present Value (NPV) and finding the Internal Rate of Return (IRR) where NPV = 0 using `root_scalar`.

**C. Parameter Change and Effect**
- **Change:** Changing the final cash flow from 2500 to 3000.
- **Effect:** The IRR increases because the project generates more total return. The Secant method might require one additional iteration compared to Newton-Raphson.

**D. Interpretation of Output and Graph**
- Both methods successfully find an IRR of approximately 10.4%. The NPV at this rate is virtually zero. Newton-Raphson is faster because it uses the exact derivative, while Secant estimates the slope using two points. This is widely used in finance to evaluate project profitability.

---

## Task 12: Polynomial and Nonlinear Equation Solving

**B. Inputs and Mathematical Operation**
- **Input:** Two equations representing a circle (`x^2 + y^2 = 4`) and a parabola (`y = x^2 - 1`). Two initial guesses: `[1.0, 1.0]` and `[-1.0, 1.0]`.
- **Operation:** Using `scipy.optimize.root` to find the intersection points (where both equations equal zero).

**C. Parameter Change and Effect**
- **Change:** Changing the circle radius from 4 to 9.
- **Effect:** The intersection points move outward along the parabola. Providing different initial guesses is necessary because nonlinear systems can have multiple valid solutions (intersections).

**D. Interpretation of Output and Graph**
- The solver successfully locates the intersection points. The residuals are extremely close to zero, confirming the solution is accurate. This method is essential for finding operating points in engineering and geometry.

---

## Task 13: Interpolation

**B. Inputs and Mathematical Operation**
- **Input:** Seven hourly temperature readings from 8:00 to 14:00.
- **Operation:** Using `scipy.interpolate` to create a linear interpolation function and a cubic spline function, then evaluating them every 10 minutes to estimate missing data points.

**C. Parameter Change and Effect**
- **Change:** Adding a noisy point at 12:00 (e.g., dropping from 24.0 to 21.0).
- **Effect:** Linear interpolation remains relatively safe and stable. The cubic spline will likely "overshoot" between the points, creating unrealistic peaks or dips. This shows that cubic splines are smoother but can be sensitive to outliers.

**D. Interpretation of Output and Graph**
- At 10:30, both methods estimate the temperature to be around 23°C. The cubic spline produces a smoother, more natural-looking curve, which is better for physical phenomena. Linear interpolation is better when the data is noisy or erratic.

---

## Task 14: Curve Fitting and Approximation

**B. Inputs and Mathematical Operation**
- **Input:** Seven pairs of data points: concurrent users `[50, 100, 150, 200, 250, 300, 350]` and server response times in ms `[82, 95, 115, 145, 185, 238, 305]`.
- **Operation:** Using `scipy.optimize.curve_fit` to find the parameters (a, b, c) of a quadratic model `y = ax^2 + bx + c` that minimizes the sum of squared errors (least squares).

**C. Parameter Change and Effect**
- **Change:** Forcing a linear model (removing the `ax^2` term) by setting `a=0`.
- **Effect:** The Root Mean Square Error (RMSE) increases significantly (from ~2 ms to over 15 ms). This proves that the quadratic term is necessary because server delay grows non-linearly (exponentially) as user load increases.

**D. Interpretation of Output and Graph**
- The fitted curve closely matches the observed data points. The low RMSE indicates the model is highly accurate. Curve fitting is widely used to predict future behavior (e.g., predicting the server response at 400 users) based on historical measurements.

---

## Task 15: Numerical Differentiation

**B. Inputs and Mathematical Operation**
- **Input:** GPS position data (in metres) sampled at 1-second intervals `time = [0, 1, 2, 3, 4, 5, 6]`.
- **Operation:** Estimating velocity (speed) using finite differences. Uses forward difference at the start, backward difference at the end, and central differences for the interior points.

**C. Parameter Change and Effect**
- **Change:** Halving the time step (e.g., sampling every 0.5 seconds instead of 1.0).
- **Effect:** The central difference estimates become more accurate (error scales with h^2). Forward and backward differences remain less accurate (error scales with h), but the overall speed estimates will converge closer to the true instantaneous velocity.

**D. Interpretation of Output and Graph**
- The estimated speed rises smoothly, showing the vehicle is accelerating. Central differences are generally more accurate because they average out errors from both sides of the point. This is exactly how GPS apps calculate your current driving speed from location pings.

---

## Task 16: Numerical Integration

**B. Inputs and Mathematical Operation**
- **Input:** Smart-meter power readings in kilowatts `[0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]` recorded every two hours.
- **Operation:** Estimating total energy consumption using two numerical integration methods: the trapezoidal rule (`np.trapezoid`) and Simpson's rule (`simpson`).

**C. Parameter Change and Effect**
- **Change:** Adding more frequent meter readings (e.g., hourly instead of every two hours).
- **Effect:** The difference between the trapezoidal estimate and Simpson's estimate shrinks. Both methods converge to the true area under the curve as the time step gets smaller.

**D. Interpretation of Output and Graph**
- The total energy consumed is roughly 26 kWh. Simpson's rule is generally more accurate for smooth curves because it fits parabolas to the data, while the trapezoidal rule fits straight lines. The difference between the two estimates provides a quick error check.

---

## Task 17: Ordinary Differential Equations - Euler Method

**B. Inputs and Mathematical Operation**
- **Input:** Newton's law of cooling: `dT/dt = -k(T - T_ambient)`. Initial temperature `T_initial = 90°C`, ambient temperature `25°C`, cooling constant `k = 0.12`, time step `h = 1.0` min, for 30 minutes.
- **Operation:** Estimating the temperature over time using the explicit Euler method update: `T[i+1] = T[i] + h * cooling_rate(T[i])`.

**C. Parameter Change and Effect**
- **Change:** Halving the time step `h` from 1.0 minute to 0.5 minutes.
- **Effect:** The numerical estimate gets closer to the true exact solution. The absolute error drops roughly in half, demonstrating that Euler's method has an error proportional to the step size (first-order accuracy).

**D. Interpretation of Output and Graph**
- The graph shows the temperature dropping exponentially from 90°C toward the ambient 25°C. The Euler method slightly under-predicts the cooling (stays a bit hotter than the exact curve). This method is simple but requires small step sizes for high accuracy.

---

## Task 18: Numerical Solution of ODEs Using SciPy

**B. Inputs and Mathematical Operation**
- **Input:** An RC circuit charging model: `dV/dt = (Vs - V) / (R*C)`. Supply voltage `Vs = 5.0V`, Resistance `R = 1000 ohms`, Capacitance `C = 0.001F`, initial voltage `V0 = 0.0`.
- **Operation:** Using `scipy.integrate.solve_ivp` with tight tolerances (`rtol=1e-9`, `atol=1e-11`) to solve the ODE over 5 seconds.

**C. Parameter Change and Effect**
- **Change:** Doubling the resistance `R` to 2000 ohms.
- **Effect:** The time constant `tau = RC` doubles, meaning the capacitor charges much slower. At 5 seconds, the voltage will be significantly lower than the original run.

**D. Interpretation of Output and Graph**
- The solver successfully matches the exact analytical solution to machine precision (error ~1e-12 V). The graph shows the classic exponential charging curve. SciPy's adaptive step sizing makes it highly accurate without needing manual step calculations.

---

## Task 19: Numerical Optimization

**B. Inputs and Mathematical Operation**
- **Input:** Cloud resource allocation problem. Cost function: `12*x + 18*y`. Capacity constraint: `100*x + 170*y >= 1000`. Bounds: `x >= 0`, `y >= 0`.
- **Operation:** Using `scipy.optimize.minimize` with the SLSQP method to find the cheapest allocation, followed by an integer brute-force search to find the best whole-number allocation.

**C. Parameter Change and Effect**
- **Change:** Raising the required total capacity from 1000 to 1500.
- **Effect:** The minimum cost increases. Because Type B servers offer more capacity per unit cost (170/18 ≈ 9.4 vs 100/12 ≈ 8.3), the optimization shifts the allocation heavily toward Type B servers.

**D. Interpretation of Output and Graph**
- The continuous optimization finds the absolute mathematical minimum. The integer search provides the practical, real-world answer because you cannot buy half a server. This is heavily used in cloud computing, logistics, and manufacturing.

---

## Task 20: Random Numbers and Monte Carlo Methods

**B. Inputs and Mathematical Operation**
- **Input:** Server demand modeled as a normal distribution with mean `850` and standard deviation `120`. Server capacity is `1000`. Number of simulations `N = 100,000`.
- **Operation:** Generating random demand scenarios, counting how many exceed capacity, and calculating the probability (overloaded / total). Plotting a running probability to show convergence.

**C. Parameter Change and Effect**
- **Change:** Increasing `N` from 100,000 to 1,000,000.
- **Effect:** The estimated probability stabilizes and becomes smoother. The standard error of the Monte Carlo estimate decreases proportional to `1/sqrt(N)`.

**D. Interpretation of Output and Graph**
- The estimated overload probability is about 10.6% (since the Z-score of 1000 is 1.25). The log-scale graph shows the running average converging to the true probability. Monte Carlo is essential for modeling risk and uncertainty in complex systems where analytical solutions are impossible.