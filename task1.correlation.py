import numpy as np
import matplotlib.pyplot as plt

# Given coordinates (x, y)
points = [
    (-5.00,  2.00),
    (-1.00,  1.00),
    ( 3.00,  1.00),
    (-3.00, -1.00),
    (-5.00, -5.00),
    (-10.00, -10.00),
    ( 1.00, -2.00),
    ( 7.00, -2.00),
    ( 5.00, -3.00),
]

x = np.array([p[0] for p in points], dtype=float)
y = np.array([p[1] for p in points], dtype=float)

# Pearson correlation coefficient
r = np.corrcoef(x, y)[0, 1]
print("Pearson correlation coefficient:", r)

# Visualization (scatter plot)
plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Correlation Analysis (r = {r:.4f})")
plt.grid(True)
plt.show()
