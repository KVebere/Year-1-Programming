from graphics import *

import math

#Notes to myself
#-Graphics windows are 200 by 200 pixels by default.
#The top-left pixel has coordinates (0, 0)
#and the bottom-right pixel is (199, 199).
#The x-values increase from left to right, and the y-values increase from top to bottom.
#-p.getX()
#-p.getY()



def helloGraphics():
    win = GraphWin()
    message = Text(Point(100, 100), "Hello graphics!")
    message.draw(win)
    win.getMouse()
    

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    leg1 = Line(Point(100, 120), Point(140, 160))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(70, 160))
    leg2.draw(win)
    arm1 = Line(Point(100, 90), Point(50, 70))
    arm1.draw(win)
    arm2 = Line(Point(100, 90), Point(150, 70))
    arm2.draw(win)


def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")
    
    
def drawCircle():
    win = GraphWin("Draw Circle")
    center = Point(100, 100)
    radius = int(input("Enter radius here: "))
    circle = Circle(center, radius)
    circle.draw(win)
    
def drawArcheryTarget():
    win = GraphWin("Archery")
    center = Point(100, 100)
    radius = 20
    
    circle3 = Circle(center, radius*3)
    circle3.setFill("blue")
    circle3.draw(win)
    
    circle2 = Circle(center, radius*2)
    circle2.setFill("red")
    circle2.draw(win)
    
    circle1 = Circle(center, radius)
    circle1.setFill("yellow")
    circle1.draw(win)
    
        
def drawRectangle():
    win = GraphWin("drawRectangle", 200, 200)
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))
    topLeftX = 100-width/2
    rectangle = Rectangle(Point(topLeftX, 100-height/2),
                          Point(topLeftX+width, 100+height/2))
    rectangle.draw(win)
    
def blueCircle():
    win = GraphWin("blue circle")
    center = win.getMouse()
    radius = 50
    circle = Circle(center, radius)
    circle.setFill("blue")
    circle.draw(win)
    
def tenLines():
    win = GraphWin("Line drawer")
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        
def tenColouredRectangles():
    win = GraphWin("tenColouredRectangles", 400, 300)
        
    inputBox = Entry(Point(200, 200), 10)
    inputBox.draw(win)
    
    for i in range(10):
    
        color = Text(Point(200, 100), "Enter colour: ")
        color.draw(win)
        
        point1 = win.getMouse()
        point2 = win.getMouse()
        rect = Rectangle(point1, point2)
        
        userInput = inputBox.getText()
        
        rect.setFill(userInput)
        
        rect.draw(win)
        
def fiveClickStickFigure():
    win = GraphWin("fiveClickStickFigure")
    p1 = win.getMouse()
    p2 = win.getMouse()
   
    radius = math.sqrt((p1.getX()-p2.getX())**2+(p1.getY()-p2.getY())**2)
    circle=Circle(p1, radius)
    circle.draw(win)
    
    p3 = win.getMouse()
    
    p6 = Point(p1.getX(), p1.getY()+radius)
    line=Line(p6, p3)
    line.draw(win)
    
    p4 = win.getMouse()
    
    dist=p1.getX()-p4.getX()
    p7=Point(p4.getX()+dist+dist, p4.getY())
    line2=Line(p4, p7)
    line2.draw(win)
    
    p5 = win.getMouse()
    
    dist2=p3.getX() - p5.getX()
    p8 = Point(p5.getX()+dist2+dist2, p5.getY())
    line3=Line(p5, p3)
    line4=Line(p8, p3)
    line3.draw(win)
    line4.draw(win)
    
 