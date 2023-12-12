class Shape:
    def area(self):
        print("Calculating Area of Geometry Shape")

class Circle(Shape):
    def area(self, radius):
        print("Area Of Circle")
        return 3.14 * radius ** 2

class Square(Shape):
    def area(self, side_length):
        print("Area Of Square")
        return side_length ** 2

shape = Shape()
circle = Circle()
square = Square()

shape.area()
circle_area = circle.area(5)
square_area = square.area(4)

print("\nCalculated Areas:")
print("Circle Area:- ",circle_area)
print("Square Area:- ",square_area)