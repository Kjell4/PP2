# volume of sphere
import math

def vol_sphere(radius):
    print((4 * math.pi * pow(radius, 3)) / 3)

R = int(input())

vol_sphere(R)