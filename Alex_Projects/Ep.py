from matplotlib import pyplot as plt
import numpy as np

def P(r, G, Mj, ml):
    return (-G*((Mj*ml)/r))

GravKo = 6.67e-11
MassJo = 5.97e24
MassMå = 7.35e22
xlist = np.linspace(1, 1000, num=1000)
ylist = P(xlist, GravKo, MassJo, MassMå)
plt.plot(xlist, ylist, c="green", label="Gravitationella lägesenergin Ep")

plt.axhline(0, color="red", linestyle="dashed", label="y = 0")

plt.xlabel("r (avstånd i meter)")
plt.ylabel("Ep (Joule)")
plt.xlim(0, )
plt.legend()
plt.show()