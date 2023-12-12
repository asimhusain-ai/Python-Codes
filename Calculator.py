def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
print("\nSELECT THE OPERATION:- \n"
      "\n1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplicatio\n"
      "4.Division\n")
choice=int(input("Enter The Choice:- "))
num1=int(input("Enter The First Number:- "))
num2=int(input("Enter The Second Number:- "))
if choice==1:
    print(add(num1, num2))
elif choice==2:
    print(subtract(num1, num2))
elif choice==3:
    print(multiply(num1, num2))
elif choice==4:
    print(divide(num1, num2))
else:
    print("Invalid")
