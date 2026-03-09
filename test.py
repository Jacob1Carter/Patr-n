from math import pow, sqrt, pi, cos, asin, sin, radians

ax, ay = 576.4080797279195, 562.1869425645145
bx, by = 460, 420
angle = radians(2)

cx = bx + (cos(angle) * (ax-bx)) + (sin(angle) * (ay-by))
cy = by - (sin(angle) * (ax-bx)) + (cos(angle) * (ay-by))

print(cx, cy)