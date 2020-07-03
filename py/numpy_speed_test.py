import numpy as np

a = 10000 * np.random.rand(100000)
b = list(a)
c = list(sorted(b))
d = sum(c)
print(d)
