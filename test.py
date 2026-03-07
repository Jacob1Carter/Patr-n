from math import pow, sqrt, pi, cos, asin

b1, b2 = 25, 25

o1, o2 = 30, 30

angle = 90

radius = (sqrt(pow(o1 - b1, 2) + pow(o2 - b2, 2)))
print(radius)

a = asin(b2/b1)
print(a)

