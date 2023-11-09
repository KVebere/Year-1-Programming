from graphics import *

def problem1():  
    sentence = input("Please enter a sentence:" ) 
    words = []  
    words = sentence.split(" ")   
    for word in words:
        print(word)
        
import random
def problem2():
    sentence = input("Please enter a sentence: ")
    words = []
    words = sentence.split(" ")
    count = len(words)
   
    win = GraphWin("Words on screen",500,500)
   
    for i in range(count):
        p = win.getMouse()
        index = random.randrange(count)
        word = words[index]
        text = Text(p, word)
        text.draw(win)
        
def problem3():
    win = GraphWin("Coordinates on screen", 500, 500)
    # Iterate over a grid patter
    for x in range(10, 500, 100):
        for y in range(10, 500, 100):
        #Wait for user input
            win.getMouse()
        # Record the coordinates in (x, y) format
            coord = f"({x},{y})"
        # Display the coordinates on the screen
            text = Text(Point(x, y), coord)
            text.setSize(8)
            text.draw(win)