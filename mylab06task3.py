import numpy as np
import math
a = float(input("Pochatok a: "))
b = float(input("Kinec b: "))
h = float(input("Krok h: "))
def f(x):
    return math.sqrt(abs(x)) + np.cbrt(x) + abs(x) ** (1/4)
x_values = np.arange(a, b + h, h)

A = []
for x in x_values:
    result = f(x)
    A.append(float(result))
print("Spisok A: ", A)

B = []
for _ in range(4):
    max_chislo = max(A)
    B.append(max_chislo)
    A.remove(max_chislo)
  
print("Spisok B: ", B)