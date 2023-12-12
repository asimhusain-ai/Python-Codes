'''
def simpleInterest(p,r,t):
    si=p*r*t/100
    return si
p=int(input("Enter Principle:- "))
r=int(input("Enter Rate:- "))
t=int(input("Enter Time Period:- "))
print ("Simple Inerest Is :- ", simpleInterest(p, t, r))
'''
#WITHOUT FUNCTION
p=int(input("Enter The Principle:- "))
t=int(input("Enter The Time Period:- "))
r=int(input("Enter The Rate:- "))
simpleinterest=p*r*t/100
print("The Simple Interest Is:-",simpleinterest)