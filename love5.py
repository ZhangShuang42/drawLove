import numpy as np
import matplotlib.pyplot as plt

a = 5.21
theta = np.linspace(0, 2*np.pi, 100)
r = a*(1 - np.sin(theta))
plt.polar(theta, r)
plt.show()
