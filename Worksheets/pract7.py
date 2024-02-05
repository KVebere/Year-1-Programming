from graphics import *
import time
import math
import random

def addUpNumbers1():
    total = 0
    more = "y"
    while more == "y": # The loop runs while `more` is "y"
        number = int(input("Enter a number "))
        total = total + number
        more = input("Any more numbers? ")
    print("The total is", total)


def addUpNumbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0: # The loop runs while `number` is not 0
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)



def addUpNumbers3():
    total = 0
    nStr = input("Number (hit enter to stop): ")
    while nStr != "": # The loop runs while `nStr` is not empty
        number = int(nStr) # Assumes that `nStr` contains a number
        total = total + number
        nStr = input("Number (hit enter to stop): ")
    print("The total is", total)



def addUpNumbers4():
    total = 0
    while True: # The loop runs until we break it
        nStr = input("Number (anything else to stop): ")
        if not nStr.isdigit():
            break # Break the loop if `nStr` is not a number
        number = int(nStr)
        total = total + number
    print("The total is", total)

def canApplyForJob(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False
    
def getPositiveNumber1():
    number = 0
    while number <= 0:
        number = int(input("Enter a positive number: "))
    return number

def getPositiveNumber2():
    while True:
        number = int(input("Enter a positive number: "))
        if number > 0:
            break
    return number

def getString1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def getString2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg

#Exercise

#Ex. 1

def getName():
    while True:
        name = str(input("Enter name here: "))
        if name.isalpha():
            break
        print("Please enter valid name!")
    return name

#Ex. 2

def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        red.setFill("red")
        amber.setFill("black")
        green.setFill("black")
        time.sleep(3)
        
        amber.setFill("yellow")
        time.sleep(1)
        
        amber.setFill("yellow")
        red.setFill("black")
        time.sleep(3)
        
        amber.setFill("black")
        green.setFill("green")
        red.setFill("black")
        time.sleep(3)
        
        amber.setFill("yellow")
        green.setFill("black")
        red.setFill("black")
        time.sleep(2)
        
#Ex.3
        
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
        
        
def gradeCoursework():
    while True:
        mark = int(input("Enter marks here to get grade(From 0-20): "))
        if mark >= 0 and mark <= 20:
            break
        print("Please enter valid mark!")
    calculateGrade(mark)
    
    
#Ex.4
    
def orderPrice():
    total = 0
    while True:
        productPrice = input(input("Enter your product prices: "))
        quantity = int(input("Enter quantity: "))
        total += productPrice * quantity
        if input("Are there more items? (y/n): ") == "n":
            break
    print(f"The total is {total:.2f} pounds")

#Ex. 5.

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
def drawBrownEye(win, centre, radius):
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius/2, "brown")
    drawCircle(win, centre, radius/4, "black")


def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    x2 = p2.getX()

    y1 = p1.getY()
    y2 = p2.getY()

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance

def clickableEye():
    win = GraphWin()
    centre = Point(100, 100)
    radius = 100
    drawBrownEye(win, centre, radius)

    while True:
        click = win.getMouse()
        clickDistance = distanceBetweenPoints(click, centre)

        if clickDistance <= radius/4:
            print("pupil")

        elif radius/4 < clickDistance <= radius/2:
            print("iris")

        elif radius/2 < clickDistance <= radius:
            print("sclera")

        else:
            break

        #Ex. 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def temperatureConverter():
    while True:
        tempType = input("Which way would you like to convert? (fahrenheit or celsius or f to stop): ")
        if tempType == "fahrenheit":
            fahrenheit = float(input("Enter temperature in fahrenheit here: "))
            celsius = fahrenheit2Celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
        elif tempType == "celsius":
            celsius = float(input("Enter temperature in celsius here: "))
            fahrenheit = celsius2Fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
        elif tempType == "f":
            break
#Ex. 7

def tableTennisScorer():
    win = GraphWin()
    line = Line(Point(100, 0), Point(100, 200))
    line.draw(win)

    score1Value = 0
    score2Value = 0

    score1 = Text(Point(50, 100), str(score1Value))
    score1.setSize(20)
    score1.draw(win)

    score2 = Text(Point(150, 100), str(score2Value))
    score2.setSize(20)
    score2.draw(win)

    while True:
        click = win.getMouse()

        if click.getX() < 100:
            score1Value += 1
            score1.setText(str(score1Value))
        elif click.getX() > 100:
            score2Value += 1
            score2.setText(str(score2Value))

        if score1Value >= 11 and score1Value - score2Value >= 2:
            winner = Text(Point(50, 150), "Player 1 wins!")
            winner.setSize(12)
            winner.draw(win)
            break
        elif score2Value >= 11 and score2Value - score1Value >= 2:
            winner = Text(Point(150, 150), "Player 2 wins!")
            winner.setSize(12)
            winner.draw(win)
            break

    win.getMouse()
    win.close()

#Ex. 8

def guessTheNumber():
    secretNum = random.randint(1, 100)

    guessCount = 0

    while guessCount<7:
        guess = int(input("Guess number from 1 to 100 "))
        if guess < secretNum:
            print("Too low")

        elif guess > secretNum:
              print("Too high")

        elif guess == secretNum:
            print("You win!")
            print("It took you", guessCount, "guesses!")

        else:
            print("You lose!")
            print("The number was", secretNum)


#Ex. 9.

 #def clickableBoxOfEyes(win, row, colums):


























    
    
        

        
        
            
        
        












