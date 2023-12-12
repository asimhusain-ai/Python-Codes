class SimpleInterest:
    def __init__(self,principal,rate,time):
        self.principal = principal
        self.rate = rate
        self.time = time
    def result(self):
        simple_interest = self.principal * self.rate * self.time / 100
        print("SI: ",simple_interest)

principal = int(input("Enter principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time: "))

si = SimpleInterest(principal,rate,time)
si.result()