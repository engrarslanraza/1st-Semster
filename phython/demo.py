"""x=int(input('enter 1st number'))
y=int(input('enter 2nd number'))
def add_sub(x,y):  
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(x,y)
print(result1,result2)"""
"""
for x in range(11):
    if(x%2==0):
        print(x,end=" ")
    else:
        print(x)
"""
"""
for i in range(10,21):
    if(i%2==0):
        print(i,end=" ")
    elif (i%3==0):
        print(i,end="\t")
    else:
        print(i,end='\n')     
"""
"""
n=1
for a in range(1,3):
    for j in range(0,a):
        print(n,end=" ")
        n=n+1
    print()
"""
"""
def integerPower(base, exponent):
    power=base**exponent
    return power
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = integerPower(base, exponent)
print("The result is:", result)
"""
"""
i = 31
while (i >= 7):
    m = i * (i-6)
    print (m,end='\n')
    i=i-8
"""
"""
balance=100
while True:
    print("welcome to atm")
    print("1:check balance")
    print("2:amount withdraw")
    print("3:amount deposite")
    print("4:exit")
    choice=int(input('enter the choice'))
    if (choice==1):
        print("your balance",balance)
    elif choice==2:
        amount=int(input('enter amount withdraw'))
        balance=balance-amount
        print('withdrawed amount',amount)
        print('remaining balance',balance)
    elif choice==3:
        amount=int(input('amount deposited'))
        balance=balance+amount
        print('deposited amount',amount)
        print('balance after deposite',balance)
    elif choice==4:
        print("thank you for using us")
        break
    else:
        print('invalid')"""


"""
a=int(input("start value"))
b=int(input("end value"))
count=0
i=a
for i in range(a,b):
    if i%5==0:
        print(i,end="\t")
        count=count+1
    if count==5:
        count=0
        print('\n')
"""
"""a=int(input("start value"))
b=int(input("end value"))
count=0
i=a
while i<b:
    if i%5==0:
        print(i,end="\t")
        count=count+1
    if count==5:
        count=0
        print("\n")
    i=i+1
    """
"""
x=int(input("Enter the Number"))
factorial=1
e=1
for i in range(1,x+1):
    factorial=factorial*i
    e=e+(1/factorial)
print("e=",e)"""
"""
x=int(input("Enter the Number"))
fact=1
e=1
i=1
while i<x:
    fact=fact*i
    e=e+(1/fact)
    i=i+1
print("e=",e)
"""
"""
n=0
sum=0
while n<10:
    x=int(input("enter Marks"))
    if x<0:
        break
    if x>100:
        continue
    n=n+1
    sum=sum+x
print(sum/10)
"""
"""
def fact(n):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact
x=int(input("enter the number"))
print(fact(x))
"""

'''
x=10
factorial=1
e=1
for i in range(1,x+1):
    factorial=factorial*i
    e=e+(1/factorial)
print("e=",e)
'''
class CoffeeMachine:
    def __init__(self):
        self.water = 1000 # ml
        self.milk = 500 # ml
        self.coffee_beans = 200 # g
        self.cups = 10 # cups

    def make_coffee(self, water, milk, coffee_beans, cost, coffee_type):
        if self.water < water:
            print("Sorry, not enough water!")
            return
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return
        if self.coffee_beans < coffee_beans:
            print("Sorry, not enough coffee beans!")
            return
        if self.cups < 1:
            print("Sorry, not enough cups!")
            return

        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.cups -= 1
        print(f"Here is your {coffee_type} coffee. Enjoy!")
        return cost

    def print_status(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee beans: {self.coffee_beans}g")
        print(f"Cups: {self.cups}")
machine = CoffeeMachine()
print(f"Total cost: ${machine.make_coffee(200, 100, 50, 100, 'hot')}") # hot coffee
print(f"Total cost: ${machine.make_coffee(150, 100, 30, 100, 'cold')}") # cold coffee
machine.print_status()

