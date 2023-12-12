class Random:
    def __init__(self, x):
        self.x = x

    def __add__(self, o):
        return self.x + o.x

obj1 = Random(2)
obj2 = Random(2)
obj3 = Random("Micheal ")
obj4 = Random("Faraday")

print("Num:- ", obj1 + obj2)
print(obj3 + obj4)