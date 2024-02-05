from graphics import *
import math
import random
from pract5 import distanceBetweenPoints



def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def canYouVote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def getDegreeClass(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31


def overlyComplexDaysInMonth(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28


def countDown():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numberedTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
        
def fastFoodOrderPrice():
    price=float(input("Enter price: "))
    print("Your order price is ", price)
    if price < 20:
        print("Your delivery fee is £2.50.")
    elif price >= 20:
        print("The delivery is free!")
    
def whatToDoToday():
    temp=float(input("Enter temperature: "))
    if temp > 25:
        print("Swimming in the sea.")
    elif temp <= 25:
        print("Shopping at Gunwharf Quays.")
        
def displaySquareRoots(start, end):
    for i in range(start, end+1):
        x = math.sqrt(i)
        print(f'The square root of {i} is {x:0.3f}')
    
def calculateGrade(mark):
    if mark >= 15 and mark <=20:
        print("A")
    elif mark >= 12 and mark <=15:
        print("B")
    elif mark >= 8 and mark <= 11:
        print("C")
    elif mark < 8:
        print("F")
    else:
        print("x")

def peasInAPod():
    number=int(input("enter a number here: "))
    win = GraphWin("", 100*number, 100)
    x=50
    y=50
    radius=50
    
    for i in range(50, 100*number, 100):
    
        circle = Circle(Point(i, y), radius)
        circle.setFill("green")
        circle.draw(win)
        
def ticketPrice(age, distance):
    if age >= 60 or age <= 15:
        discount = 0.40
    else:
        discount = 0
    ticketPrice = 10 + (distance * 0.15)
    discountedPrice = float(ticketPrice * (1 - discount))
    return discountedPrice
    
        
def numberedSquare(n):
    for i in range(n):
        #print("{0} {1} {2} {3}\n".format(n - i, n - i + 1, n - i + 2, n - i + 3))
        print(f"{n-i} {n-i+1} {n-i+2} {n-i+3}\n")

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    

def drawColouredEye(win, centre, radius, colour):
    #win = GraphWin()
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, "black")
    
def eyePicker():
    win = GraphWin("Eye picker", 400, 400)
    colours = ["blue", "grey", "green", "brown"]
    centreX = int(input("Enter x: "))
    centreY = int(input("Enter y: "))
    centre = Point(centreX, centreY)
    colour = input("Enter colour: ")
    radius = int(input("Enter radius: "))
    if centreX > 400 and centreY > 400:
        print("Eye centre not in window.")
    elif colour not in colours:
        print("Invalid colour.")  
    else:
      drawColouredEye(win, centre, radius, colour)
      
#Ex. 9

def rectangle(win, x, y, colour):
    #win = GraphWin("", 200, 200)
    p1 = Point(x, y)
    p2 = Point(x + 20, y + 20)
    rectangles = Rectangle(p1, p2)
    rectangles.setOutline(colour)
    rectangles.draw(win)
    return rectangles

def text(win, x, y, string, colour, size):
    #win = GraphWin("", 200, 200)
    p1 = Point(x, y)
    texts = Text(p1, string)
    texts.setOutline(colour)
    texts.setSize(size)
    texts.draw(win)
    return texts

def circle(win, centre, radius, colour):
    circles = Circle(centre, radius)
    circles.setOutline(colour)
    circles.draw(win)


def drawpatchwindow2():
    win = GraphWin()
    for radius in range(50, 5, -10):
        for y in range(50, 5, -10):
            circle(win, Point(50, 50), radius, "red")



# def drawpatchwindow():
#     win = GraphWin()
#     win.setBackground("white")
#     for x in range(0, 100, 20):
#         for y in range(0, 100, 20):
#             rectangle(win, x, y, "red")
#             text(win, x+10, y+10, "hi!", "red", 10)
#
def drawpatchwindow():
    win = GraphWin()
    for y in range(5, 100, 5):
        circle(win, Point(50, 50-y), y-50, "red")


# def a():
#     win = graphwin("aa", 500, 500)
#
#     for x in range(0, 500, 100):
#         for y in range(0, 500, 100):
#             rectangle(win, x, y, "red")


def drawpatchwindow():
    win = GraphWin()

              

def eyesAllAround():
    win = GraphWin("", 500, 500)
    colour="blue"
    for i in range(30):
        centre = win.getMouse()
        if colour == "blue":
            colour ="grey"
        elif colour == "grey":
            colour = "green"
        elif colour == "green":
            colour = "brown"
        else:
            colour = "blue"

        drawColouredEye(win, centre, 30, colour)

#Task 12

def archeryGame():
    win = GraphWin()
    drawCircle(win, Point(100, 100), 20 * 3, "blue")
    drawCircle(win, Point(100, 100), 20 * 2, "red")
    drawCircle(win, Point(100, 100), 20, "yellow")
    score = 0

    for i in range(5):
        arrow = win.getMouse()
        horizontal_deviation = random.randint(-5, 5)
        vertical_deviation = random.randint(-5, 5)
        arrow.x += horizontal_deviation
        arrow.y += vertical_deviation
        target_center = Point(100, 100)
        distance = distanceBetweenPoints(target_center, arrow)

        if distance <= 20:
            score += 10
        elif 20 < distance <= 30:
            score += 5
        elif distance > 30:
            score += 2

        drawCircle(win, arrow, 1, "black")
    score_text = Text(Point(100, 20), f"Total Score: {score}")
    score_text.setSize(10)
    score_text.draw(win)




    


        
        
        
    

    
    
