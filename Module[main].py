# Import the Module_Geometry module
import Module_Geometry
radius = 5
circle_result = Module_Geometry.circle_area(radius)
print(f"Area Of Circle:- {circle_result:.2f}")

side = 4
square_result = Module_Geometry.square_area(side)
print(f"Area Of Square:-  {square_result}")

length = 6
width = 8
rectangle_result = Module_Geometry.rectangle_area(length, width)
print(f"Area Of Rectangle:-  {rectangle_result}")

base = 3
height = 7
triangle_result = Module_Geometry.triangle_area(base, height)
print(f"Area Of Triangle:-  {triangle_result}")

base1 = 4
base2 = 6
trapezoid_height = 5
trapezoid_result = Module_Geometry.trapezoid_area(base1, base2, trapezoid_height)
print(f"Area Of Trapezoid:-  {trapezoid_result}")
