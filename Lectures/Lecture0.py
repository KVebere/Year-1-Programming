#Receives a number from console
#Adds 2 to that number
#Prints result

def add2():
    x = int(input("please enter an integer: "))
    y = x + 2
    print("result is ", y)
    
#Receives a number, x, from console
#Calculates y = 3*x + 2
#Prints y
def calcStrightLine():
    x = int(input("please enter an integer: "))
    y = 3*x + 2
    print("result is ", y)

#Receives a number from console
#Creates a loop using the number
#Adds up all numbers up to but not including that number
#Prints sum

def firstLoopEx():
    loopCounter = int(input("please enter an integer: "))
    
    for i in range(loopCounter):
        print("current value if i is ",i)
        
#Receives a number, n,  from console
#Creates a loop using the number, n
#Enters n values into a list []
#Prints sum of all items in list using loop
        
def calculateListSum():
    n = int(input("please enter an integer: "))
    numbers = []
    
    for _ in range(n):
        value = int(input("Enter a number: "))
        numbers.append(value)
        
    total = 0
    for num in numbers:
        total += num
        
    print("The sum is: ", total)


    