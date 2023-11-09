def sayHello():
    print("Hello World")

def sayBye():
    print("Goodbye Mars")
    
# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
    
def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print("The weight in ounces is ", ounces)
        
def count():
    for number in range(10):
        print("Number is now: ", number)
        
def sayName():
    print("Keita Vebere")
    
def sayHello2():
    print("Hello")
    print("World")
    
def dollars2Pounds():
    dollars = float(input("Enter value in dollars:"))
    pounds = 0.80 * dollars
    print("The value in pounds is", pounds)
    
def tenHellos():
    for i in range (11):
        print("Hello World")
        
def railFareIncrease():
    price = 16.50
    print(price)
    for i in range(11):
        price = price * 1.02    
        print(i, price)
        
        
def countTo():
    num=int(input("Enter a number: "))
    for num in range(num):
        num = num + 1  
        print(num)
       
        
def countFromTo():
    start = int(input('Enter a start value: '))
    end = int(input('Enter an end value: '))
    for start in range(end):
        start = start + 1  
        print(start)
        
def changeCounter():
    onePence = float(input('Enter a change value: '))
    twoPence = float(input('Enter a change value: '))
    fivePence = float(input('Enter a change value: '))
    pence = onePence + 2  * twoPence + 5*fivePence
    print("The total amount of money in pence is", pence)
    
def weightsTable():
    print("===================")
    for kgs in range(10, 60, 10):
        ounces = 35.274 * kgs
        print(kgs, "|" ,ounces)
        
def weightsTable2():
    print(f"{'Kgs': <5}| {'Ounces':<5} ")
    for i in range
    

def futureRailFare():
    price = float(input("Enter the initial fare: "))
    months = int(input("Enter number of months: "))
    print(price)
    for i in range(months):
        price = price * 1.02    
        print("The fare after", i+1, "is £", price)        

        

    
        