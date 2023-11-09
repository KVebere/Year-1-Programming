import math

def areaOfRectangle():
    length = float(input("length:"))
    height = float(input("height (meters):"))
    
    area = length * height
    print("the area is", area, "meters squared")
    


def areaOfRectangle2():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    length = x2-x1
    height = y2-y1
    
    area = length * height
    print("the area is", area, "meters squared")
    
def fibonacci():
    fib1 = 1
    fib2 = 1
    for i in range(1):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        print(fib3, fib2, fib1)
        

    
    
    
def distanceBetweenPoints():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    dx = x2 - x1
    dy = y2 - y1
    
    dxSq = dx * dx
    dySq = dy * dy
    
    added = dxSq + dySq
    
    distance = math.sqrt(added)
    
    print("the distance is ", distance)
    
    
    
    
    
def slope():
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    dx = x2 - x1
    dy = y2 - y1
    
    slope = dy/dx 
    
    print("slope: ", slope)