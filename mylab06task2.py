import numpy as np
import math

a=float(input("Pochatok a: "))
b=float(input("Kinec b: "))
h=float(input("Krok h: "))

def f(x):
    return math.sqrt(abs(x))+np.cbrt(x)+abs(x)**(1/4)

x_values=np.arange(a, b+h, h)

i=0
while i < len(x_values):
    x=x_values[i]
    result=f(x)
    print("%i x=%.1f f(x)=%.5f" % (i, x, result))
    i+=1 

