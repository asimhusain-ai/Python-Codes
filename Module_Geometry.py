import math

def circle_area(radius):
    return math.pi * radius**2

def square_area(side):
    return side**2

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height
