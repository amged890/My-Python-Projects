import numpy as np

x = [1, 2, 3, 4]
x = np.array(x)
print((type(x)))
print(x)

values = [22.5, 24.9, 27.8, 27.1]
varray = np.array(values)

conversion = varray * 1.8 + 32
print(conversion)
print(varray[0])

print(list(conversion))
