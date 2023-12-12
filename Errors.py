''' T Y P E   E R R O R '''
def addition(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Cannot add Different Types"

result = addition("A", 3)
print("The Result Is:- ", result)
print("-----------------")

''' I N D E X   E R R O R '''
list = [2,3,4,5,6]
try:
    print(list[6])
except:
    print("Index Error")
print("-----------------")

''' V A L U E   E R R O R '''
x = input("Enter a number: ")
try:
    number = int(x)
    print("The Entered Number Is:", number)
except ValueError:
    print("Error: Please Enter a Valid Integer")
print("------------------")

''' A T T R I B U T E   E R R O R '''
class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")
try:
    trick = dog.trick
    print("Trick:- ", trick)
except AttributeError:
    print("Error: Dog Doesn't Know Any Tricks")