import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from mpi4py import MPI

y = np.array([4, 6, 6, 4, 4, 5])
x = np.array([0, 2, 4, 6, 8, 10])

# Area using the formula h/2((y0 + yn) + 2(y1+y2 ... yn-1)) with n = 5
area = 2/2 * ((4 + 5) + 2 * (6 + 6 + 4 + 4))
print("Area Under the Curve Via Trapezium Rule is ", area, "Units Squared")

# Display the Curve in MatplotLib
xnew = np.linspace(x.min(), x.max(), 1000)
spl = make_interp_spline(x, y, k=3)
ynew = spl(xnew)
plt.figure(figsize=(7, 5))
plt.grid()
plt.ylim(0, 7)
plt.xlim(0, 10)
plt.fill_between(xnew, ynew)
plt.plot(xnew, ynew)
plt.show()
