import numpy as np
import itertools


def fac(i):
    if i == 0:
        return 1
    return fac(i - 1) * i

n = 4
k = 2
v = fac(n) * (0.5 ** k) * (0.5 ** (n - k)) / (fac(k) * fac(n - k))

k, n = 0, 1000
a, b, c, d = np.random.randint(0, 2, n), np.random.randint(0, 2, n), np.random.randint(0, 2, n), \
             np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(n):
    if x[i] == 2:
        k += 1
print(k, n, k / n, v)


"""ex04"""
n = 0
for p in itertools.product("12345", repeat=3):
    n += 1
    print(n, ''.join(p))
