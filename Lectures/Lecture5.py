from graphics import *
from time import *

def main():
    win=GraphWin("",500,300)
    car=[]
    
    #carTop
    xTL = 100
    yTL = 130
    wCarTop=100
    hCarTop = 50
    
    colourCar="blue"
    
    topLeft = Point(xTL, yTL)
    bottomRight = Point(xTL+wCarTop, yTL+hCarTop)
    carTop=Rectangle(topLeft, bottomRight)
    carTop.setFill(colourCar)
    carTop.draw(win)
    car.append(carTop)
    diff=30
    
    #carBody
    topLeft = Point(xTL-diff, yTL+hCarTop)
    bottomRight = Point(xTL+wCarTop +diff, yTL+hCarTop + hCarTop)
    carTop=Rectangle(topLeft, bottomRight)
    carTop.setFill(colourCar)
    carTop.draw(win)
    car.append(carTop)
    
    #leftWheel
    center=Point(xTL, yTL+hCarTop + hCarTop)
    radius= hCarTop/2
    whiteCircle=Circle(center, radius)
    whiteCircle.setFill("black")
    whiteCircle.draw(win)
    car.append(whiteCircle)
    
    radius= radius - 10
    whiteCircle=Circle(center, radius)
    whiteCircle.setFill("white")
    whiteCircle.draw(win)
    car.append(whiteCircle)
    
    #rightwheel
    center=Point(xTL+wCarTop, yTL+hCarTop + hCarTop)
    radius= hCarTop/2
    whiteCircle=Circle(center, radius)
    whiteCircle.setFill("black")
    whiteCircle.draw(win)
    car.append(whiteCircle)
    
    radius= radius - 10
    whiteCircle=Circle(center, radius)
    whiteCircle.setFill("white")
    whiteCircle.draw(win)
    car.append(whiteCircle)
    
    for _ in range(1000):
        sleep(.01)
        for carPart in car:
            carPart.move(1, 0)
    
    
    
    
     
