def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
x=int(input("Enter x Value:-"))
y=int(input("Enter y Value:-"))
print("Before:- ",x," ",y)
swapping = swap(x,y)
print("After:- ",swapping)