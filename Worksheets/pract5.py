import math
from graphics import *

def greet(name):
    print(f"Hello, {name}!")
    
#def main():
    myName=input("What is your name? ")
    greet(myName)
    
#def main(): 
    myName=input("What is your name? ")
    greeting = greet(myName)
    print(greeting)


def product(a, b):
    return a * b

def divide(a, b):
    return a/b

def divideAndProduct(a, b):
    productResult = product(a, b)
    divideResult = divide(a, b)
    return productResult, divideResult

def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate) 
    return amount


def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calcFutureValue(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)

#Programming exercises
 
def areaOfCircle(radius):
    return math.pi * radius ** 2

def circumferenceOfCircle(radius):
    return 2*math.pi*radius

def circleInfo():
    radius=float(input("Enter radius here: "))
    area = areaOfCircle(radius)
    circumference= circumferenceOfCircle(radius)
    output = f"Area of the circle is {area:0.3f} cm"
    output += f" and circumference is {circumference:0.3f} cm"
    print(output)
    
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    
def drawBrownEyeInCentre():
    win = GraphWin()
    centre = Point(100, 100)
    drawCircle(win, centre, 60, "white")
    drawCircle(win, centre, 30, "brown")
    drawCircle(win, centre, 15, "black")

def drawBrownEye(win, centre, radius):
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius/2, "brown")
    drawCircle(win, centre, radius/4, "black")
        
def drawBlockOfStars(number, rows):
    for i in range(rows):
        print("*"*number)
        
def drawLetterE():
    drawBlockOfStars(8, 2)
    drawBlockOfStars(2, 2)
    drawBlockOfStars(5, 2)
    drawBlockOfStars(2, 2)
    drawBlockOfStars(8, 2)
    

def drawPairOfBrownEyes():
    win = GraphWin("", 400, 200)
    drawBrownEye(win, Point(140, 100), 60)
    drawBrownEye(win, Point(260, 100), 60)
    #for i in range(2):
    #    drawBrownEyeInCentre()
        
            
 
def distanceBetweenPoints(p1, p2):
    
    x1=p1.getX()
    x2=p2.getX()
    
    y1=p1.getY()
    y2=p2.getY()
        
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    return distance
    
def distanceCalculator():
    win = GraphWin()
    message = Text(Point(100, 100), "Click on first location")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second location")
    p2 = win.getMouse()
    dist = distanceBetweenPoints(p1, p2)
    message.setText(f"{dist}")
    
    
def drawBlocks(space1, number1, space2, number2, rows):
    for i in range(rows):
        print(" "*space1, "*"*number1, " "*space2,"*"*number2)
        #The draw block does not seem to be working in correct way.
        #seems to ignore spaces when called upon? 

def drawLetterA():
    drawBlocks(1, 4, 0, 4, 2)
    drawBlocks(0, 2, 6, 2, 2)
    drawBlocks(0, 5, 0, 5, 2)
    drawBlocks(0, 2, 6, 2, 3)
   

        
def drawFourPairsOfBrownEyes():
    win = GraphWin("", 400, 400)
    
    for i in range(2):
        p1=win.getMouse()
        p2=win.getMouse()
        radius=distanceBetweenPoints(p1, p2)
        centre2=Point(p1.getX()+radius+radius,  p1.getY())
        drawOneBrownEye(win,p1, radius)
        drawOneBrownEye(win,centre2, radius)
        
    win.getMouse()
    
        
    
def displayTextWithSpaces(string, size, position, win):
    displayString=""
    for letter in string:
        displayString+=letter+" "
    displayString= displayString[0:-1]
    stringDisplay=Text(position, displayString)
    stringDisplay.setSize(size)
    stringDisplay.draw(win)
        
def drawStickFigureFamily(win, point, size):
    win = GraphWin("Stick figure fam")
    
def constructVisionChart():
    win=GraphWin()
    size=30
    y=30
    for i in range(6):
        string=input("enter string: ").upper()
        displayTextWithSpaces(string, size, Point(100, y), win)
        size-=5
        if(y<90):
            y+=30
        else:
            y+=20
        
def drawStickFigure(win, position, size):
    radius = size * 4
    head = Circle(position, radius)
    head.draw(win) 
    upperBodyPoint = Point(position.getX(), position.getY() + radius) 
    lowerBodyPoint = Point(position.getX(), upperBodyPoint.getY() + 2 * radius) 
    body = Line(upperBodyPoint, lowerBodyPoint)
    body.draw(win) 
    limbLength = size * 5 
    leftLimbX = position.getX() - limbLength
    rightLimbX = position.getX() + limbLength
    armY = upperBodyPoint.getY() + radius
    leftArmPoint = Point(leftLimbX, armY) 
    rightArmPoint = Point(rightLimbX, armY)
    arms = Line(leftArmPoint, rightArmPoint)
    arms.draw(win) 
    legY = lowerBodyPoint.getY() + limbLength
    rightLegPoint = Point(rightLimbX, legY) 
    leftLegPoint = Point(leftLimbX, legY)
    rightLeg = Line(lowerBodyPoint, rightLegPoint)
    rightLeg.draw(win)
    leftLeg = Line(lowerBodyPoint, leftLegPoint)
    leftLeg.draw(win)
    
def drawStickFigureFamily():
    win = GraphWin("Stick Figure Family", 500, 500)
    drawStickFigure(win, Point(100, 50), 5)
    drawStickFigure(win, Point(250, 50), 5)
    drawStickFigure(win, Point(400, 50), 5)
    drawStickFigure(win, Point(175, 200), 4)
    drawStickFigure(win, Point(325, 200), 4)
        
    
    

    
    
    


    


    
        
        


    
   
    
    

    
    


    
     
        
        

       

    
    
    







