import math

def circle_area(radius):
    return math.pi * radius**2

radius = int(input("Enter the radius of the circle: "))
result = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {result}")

def rectangle_area(length, width):
    return length * width

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
result = rectangle_area(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {result}")

