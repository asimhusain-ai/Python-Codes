a = float(input("Enter Value:- "))
b = float(input("Enter Value:- "))
c = float(input("Enter Value:- "))
roots = b * b - 4 * a * b
if roots > 0:
    print("Real And Distinct")
elif roots == 0:
    print("Real And Same")
else:
    print("Complex")