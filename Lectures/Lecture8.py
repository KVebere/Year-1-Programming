from graphics import *

def drawRectangle(win, x, y, size, colour):
    topLeft = Point(x, y)
    bottomRight = Point(x+size, y+size)
    rectangle = Rectangle(topLeft, bottomRight)
    rectangle.setFill(colour)
    rectangle.draw(win)
    return rectangle


def colourSelector(point, width, height):
    colours = ["blue", "red", "yellow", "green"]
    x = point.getX()
    y = point.getY()
    hWidth = width/2
    hHeight = height/2
    
    if x < hWidth and y < hHeight :
        return colours[0]
    elif x >= hWidth and y < hHeight:
        return colours[1]
    elif x < hWidth and y >= hHeight:
        return colours[2]
    else:
        return colours[3]
 


def main():
    width = 500
    height = 400
    size = 20
    hWidth = width/2
    hHeight = height/2
    win = GraphWin("", width, height)
    
    for y in range(0, int(hHeight), size):
        for x in range(0, int(hWidth), size):
          point = win.getMouse()
          colour=colourSelector(point, hWidth, hHeight)
        #win.setBackground(colour)
          drawRectangle(win, x, y, size, colour)
    




main()