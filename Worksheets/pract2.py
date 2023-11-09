import math


def squareRootCalculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers.")
    else:
        sqrtValue = math.sqrt(num)
        print("Square root:", round(sqrtValue, 2))


def sineAndCosine():
    angle = float(input("Enter an angle in degrees: "))
    angleInRadians = math.radians(angle)  # converts degrees to radians
    sineValue = math.sin(angleInRadians)
    cosineValue = math.cos(angleInRadians)
    print("Sine of the angle:", round(sineValue, 2))
    print("Cosine of the angle:", round(cosineValue, 2))


def speedCalcilator():
    km = float(input("Enter distance in km here: "))
    h = float(input("Enter duration in hours here: "))
    km/h == km / h
    print("The speed is", km/h)
    

def circumferenceOfCircle():
    radius = float(input("Enter radius here: "))
    circumference = 2*math.pi*radius
    print("The circumference of the circle is: ", circumference)
    
    
    
def areaOfCircle():
    radius = float(input("Enter radius here: "))
    area = math.pi*radius**2
    print("The area of the circle is: ", area)
    
  
def costOfPizza():
    size = float(input("Enter the size of pizza in cm: "))
    pizza = math.pi*size**2
    cost = pizza*3.5/100
    print("The cost of pizza is", cost, "pounds")
    
    
def slopeOfLine():
    x1 = float(input("Enter x1 value here: "))
    y1 = float(input("Enter y1 value here: "))
    x2 = float(input("Enter x2 value here: "))
    y2 = float(input("Enter y2 value here: "))
    
    dx = x2 - x1
    dy = y2 - y1
    
    slope = dy/dx 
    
    print("slope: ", slope)
    
    
def distanceBetweenPoints():
    x1 = float(input("Enter x1 value here: "))
    y1 = float(input("Enter y1 value here: "))
    x2 = float(input("Enter x2 value here: "))
    y2 = float(input("Enter y2 value here: "))
    
    dx = x2 - x1
    dy = y2 - y1
    
    dxSq = dx * dx
    dySq = dy * dy
    
    added = dxSq + dySq
    
    distance = math.sqrt(added)
    
    print("the distance is ", distance)
    
    
def travelStatistics():
    speed = float(input("Enter speed in km/h here: "))
    hours = float(input("Enter duration in hours here: "))
    distance = speed * hours
    fuel = distance*5
    
    print("Distance travelled: ", distance, "km")
    print("Fuel used: ", fuel, "litres")
    
def averageOfNumbers():
    number = int(input("Enter amount of numbers:  "))
    sum = 0
    for i in range(number):
        num = int(input("num: "))
        sum = sum + num

    average = sum / number_in_series
    print(average)
    
    
def fibonacci():
    n = int(input("Enter n number here: "))
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
        

def selectCoins():
    twopound = 200
    onepound = 100
    fiftyp = 50
    twentyp = 20
    tenp = 10
    fivep = 5
    twop = 2
    onep = 1
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    money = int(input('Enter how much money you have in pence: ')) 
    a, money = money // twopound, money % twopound 
    b, money = money // onepound, money % onepound 
    c, money = money // fiftyp,   money % fiftyp   
    d, money = money // twentyp,  money % twentyp 
    e, money = money // tenp,     money % tenp     
    f, money = money // fivep,    money % fivep    
    g, money = money // twop,     money % twop     
    e, money = money // onep,     money % onep     
    print(a,b,c,d,e,f,g,h)
        

    
    
    
    
    
    
    

    
 
 





