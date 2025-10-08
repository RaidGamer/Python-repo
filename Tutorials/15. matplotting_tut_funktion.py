import matplotlib.pyplot as plt
import numpy as np

def f(x, a, b, c):
    return a*x**2+b*x+c

xlist = np.linspace(-20, 20, num=1000)
#xlist = np.arrange(-20, 10.1, .1)

ylist = f(xlist, 3, 2, 4)

plt.figure(num=0, dpi=120)
plt.plot(xlist, ylist)
plt.title("Funktions exempel")
plt.xlabel("X-Axeln")
plt.ylabel("Y-Axeln")
plt.show()