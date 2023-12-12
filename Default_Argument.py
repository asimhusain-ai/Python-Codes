def triangle_area(base, height=1):
    return 0.5 * base * height

x = int(input("Enter Base:- "))
area = triangle_area(x)
print(f"Triangle Area:-  {area}")
