from math import pow, sqrt, pi, cos, asin, sin, radians


#radius = sqrt(pow(o1 - b1, 2) + pow(o2 - b2, 2)) ignore


ax, ay = 5, 16
cx, cy = 5, 6
b = radians(110)

bx = cx + (cos(b) * (ax-cx)) + (sin(b) * (ay-cy))
by = cy + (sin(b) * (ax-cx)) + (cos(b) * (ay-cy))

print(bx, by)
exit()



B = sqrt(
    (2*pow(A, 2)) * (1 - cos(b))
)
print(B)

a_dist = (B**2 - A**2 + A**2) / (2 * A)
points_dist = sqrt(B**2 - a_dist**2)
print(points_dist)