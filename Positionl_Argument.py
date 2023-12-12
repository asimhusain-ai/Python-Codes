def triangle_area(base, height):
    return 0.5 * base * height

x = int(input("Enter Base:- "))
y = int(input("Enter Height:- "))

area = triangle_area(x, y)
print(f"Triangle area:- {area}")