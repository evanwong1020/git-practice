import math

x = math.pi

print("Area of circles with different radius:")

for r in range(10):
    print("Radius: " , r , " - area: " , str(x*math.pow(r,2)))