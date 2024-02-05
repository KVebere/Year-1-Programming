from graphics import *

# List example:
def displayMonths():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in months:
        print(month)


# List example:
def displayTemperatureOfWeek():
    temperatures = [14.5, 8.0, -2.5, 15.0, 12.5, 9.0, -1.0]
    for temp in temperatures:
        print("It's {} degrees today".format(temp))
        if temp < 0:
            print("Brrrrr, that's freezing!")


# List example:
def processNumbers():
    numbers = [11, 28, 32, 34, 45, 67, 70, 89, 90, 99]
    for i in range(len(numbers)):
        if i % 2 == 0:  # Only process numbers at even indexes
            square = numbers[i] ** 2
            print("The square of {} is {}".format(numbers[i], square))


# List example:
def readPrime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        num = int(input("Enter a prime number less than 20: "))
        if num in primes:
            break
    print(num, "is a prime number less than 20")


# List example:
def changeColours():
    win = GraphWin()
    circles = []
    for x in range(50, 200, 100):
        for y in range(50, 200, 100):
            circle = Circle(Point(x, y), 50)
            circle.setFill("red")
            circle.draw(win)
            circles.append(circle)  # Add the circle to the list

    for circle in circles:  # For each circle in the list
        win.getMouse()  # Wait for a mouse click
        circle.setFill("green")  # Change the colour of the circle


# List of tuples example:
def displayMenu():
    menu = [("Chicken Tikka Masala", 900, 8.95),
            ("Lamnb Rogan Josh", 700, 7.95),
            ("Vegetable Biryani", 600, 6.95),
            ("Portion of poppadoms", 100, 0.75)]
    for item in menu:
        name, calories, price = item
        print("{:20} {:5} calories, £{:4.2f}".format(name, calories, price))


# Set example:
def filterFruits():
    fruits = {"apple", "banana", "kiwi", "pear", "orange"}
    fruitsILike = set()  # Create an empty set
    for fruit in fruits:
        if fruit != "kiwi" and fruit != "pear":
            fruitsILike.add(fruit)
    print(fruitsILike)


# Dictionary example:
def iterateStudents():
    studnets = {
        3419903: "Lou",
        7470773: "Nannie",
        5285384: "Hester"
    }
    for upNum in studnets:
        name = studnets[upNum]
        print("UP{} is {}".format(upNum, name))


#------------------------------------------------------
#EX1

def displayDate(date, month, year):
    monthList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if int(month) in range(1,13):
        month_name = monthList[int(month)-1]
        return f"{date}, {month_name}, {year}"
    else:
        "Please enter valid data!"

#EX2
def wordLengths(word_list):
    for word in word_list:
        print(f"{word}, {len(word)}")

#EX3
def drawHexagon():
    win = GraphWin()

    nodes = []
    for i in range(6):
        point = win.getMouse()
        nodes.append(point)
        point.draw(win)

    hexagon = Polygon(nodes)
    hexagon.setFill("red")
    hexagon.draw(win)

#EX4
def testMarks():
    marks_list = []
    while True:
        mark = input("Enter mark here or f to finish: ")
        if mark == "f":
            break

        mark = int(mark)
        if 0 <= mark <= 5:
            marks_list.append(mark)
        else:
            print("Invalid!")

    counts = [marks_list.count(i) for i in range(6)]

    for i, count in enumerate(counts):
        print(f"{count} student(s) got {i} marks")

#Ex5

def drawBarChart(data):
    max_value = max(data)

    for i in range(1, max_value+1):
        row = ''

        for value in data:
            row += '#' if value >= i else ' '
        print(row)



