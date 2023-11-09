from graphics import *


def drawRectangle(window):

    point1 = window.getMouse()
    point2 = window.getMouse()

    rect = Rectangle(point1, point2)
    rect.setFill("blue")

    rect.draw(window)
    
    
def drawCircle(window):

    center = window.getMouse()
    radius = 50

    circle = Circle(center, radius)
    circle.setFill("purple")

    circle.draw(window)
    
def drawLine(window):

    p1 = window.getMouse()
    p2 = window.getMouse()

    line = Line(p1, p2)

    line.setFill("black")
    line.draw(window)


def main():

    width = int(input("Width: "))
    height = int(input("Height: "))

    win = GraphWin("Hamster", width, height)

    for i in range(5):
        drawLine(win)

    win.mainloop()





######################## EXECUTE MAIN  ###########################
main()