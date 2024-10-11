import numpy as np
import math

a=float(input("Pochatok a: "))
b=float(input("Kinec b: "))
h=float(input("Krok h: "))

def f(x):
    return math.sqrt(abs(x))+np.cbrt(x)+abs(x)**(1/4)

x_values = np.arange(a, b + h, h)

for i, x in enumerate(x_values):
    result=f(x)
    print("%i x=%.1f f(x)=%.5f" % (i, x, result))


