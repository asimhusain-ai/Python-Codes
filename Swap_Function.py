def swap(x,y):
    temp = x
    x = y
    y = temp
    return x, y
x = int(input("Enter 1st No:- "))
y = int(input("Enter 2nd No:- "))
swapping = swap(x,y)
print("After Swapping:- ",swapping)