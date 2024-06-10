from graphics import *

def drawCircle():
    width = 400
    height = 100
    win = GraphWin("Circles", width, height)
    for i in range(20):
        centre = win.getMouse()
        
        if centre.getX() < 200 and centre.getY() < 100 :
            colour=""
        
        elif centre.getX() >= 300 and centre.getY() < 100:
             colour="green"
        else:
            colour="blue"
        
        circle = Circle(centre, 10)
        #circle.setFill(colour)
        circle.setOutline("black")
        circle.setWidth(2)
        circle.setFill(colour)
        circle.draw(win)
        
def drawCircle2():
    width = 400
    height = 100
    win = GraphWin("Circles", width, height)

