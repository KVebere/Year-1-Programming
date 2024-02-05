from graphics import *

def testPoint():
    p = Point(100, 50)
    print("p is of type:", type(p))  # <class 'graphics.Point'>
    
    print("p's x coordinate is", p.getX())  # 100
    print("p's y coordinate is", p.getY())  # 50
    p.move(10, -20)
    print("p's x coordinate is", p.getX())  # 110
    print("p's y coordinate is", p.getY())  # 30
    print("p is:", p)  # Point(110.0, 30.0)

#testPoint() 
    
class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output
        

def testMyPoint():
    myPoint = MyPoint(100, 50)
    myPoint.move(10, -20)
    print("myPoint's x coordinate is", myPoint.getX())
    print("myPoint's y coordinate is", myPoint.getY())
    print("myPoint is: ", myPoint)
#testMyPoint()

class Square:

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side 
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fillColour = "black"
        self.outlineColour = "black"

    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2
    
    def getPerimeter(self):
        calculate = self.side * 4
        return calculate
    
    def getArea(self):
        calculate = self.side**2
        return calculate
    
    def getSide(self):
        return self.side
    
    def getCenter(self):
        centerX = (self.p1.getX() + self.p2.getX())/2
        centerY = (self.p1.getY() + self.p2.getY())/2
        calculate = MyPoint(centerX, centerY)
        return calculate
    
    def scale(self, number):
        self.new_side = self.side * number 
        self.p2 = MyPoint(self.p1.getX() + self.new_side, self.p1.getY() + self.new_side)
        return self
    
    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output
    
    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fillColour = colour
    
    def setOutlineColour(self, colour):
        colours = ["red", "green", "blue"]
        if colour in colours:
            self.outlineColour = colour
    
def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    square.move(10, -20)
    
    # print("square's side length is", square.getSide())  # 50
    # print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    # print("square's p2 is", square.getP2())  # MyPoint(150, 100)
    # print(square)

    # square.setFillColour("red")
    # print("square's fill colour is", square.fillColour)
    # square.setOutlineColour("blue")
    # print("square's outline colour is", square.outlineColour)

    # print("Perimeter of the square is ", square.getPerimeter())
    # print("Area is", square.getArea())
    print("The centre is", square.getCenter())
    print("After scaling the square is:", square.scale(5)) 
#testSquare()

class MyCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def getCenter(self):
        return self.center 

    def getRadius(self):
        return self.radius
    
    def move(self, dx, dy):
        self.center.move(dx, dy)

    def __str__(self):
        return f"Square({self.center}, {self.radius})"


def testCircle(): #feedback
    center = MyPoint(50, 50)
    radius = 50
    circle = MyCircle(center, radius)

    print("Center: ", circle.getCenter())
    print("Radius: ", circle.getRadius())

    circle.move(10, -20)

    print("New center: ", circle.getCenter())
    print("Radius: ", circle.getRadius())

    print(circle)

#testCircle()

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name
    
    def deposit(self, money):
        self.balance += money 
        return self.balance
    
    def withdraw(self, money):
        self.balance -= money
        return self.balance
    
    def interestRate(self, time):
        calculate = self.balance * 0.5 * time
        return calculate
    
    
def testAcc():
    name = "Keita Vebere"
    balance = 10.00
    myAccount = Account(name, balance)

    print("Account holder: ", myAccount.getName())
    print("Balance: ", myAccount.getBalance())
    
    myAccount.deposit(50)
    print("Balance after deposit: ", myAccount.getBalance())
    myAccount.withdraw(20)
    print("balance after withdraw: ", myAccount.getBalance())

#testAcc()
    
class Aeroplane:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination
        self.fuel = 0 
        self.altitude = 0

    def setFuel(self, number):
        self.fuel += number
        return self.fuel 
    
    def getFuel(self):
        return self.fuel
    
    def increaseAltitude(self, number):
        self.altitude += number
        return self.altitude
    
    def decreaseAltitude(self, number):
        self.altitude -= number
        return self.altitude
    
    def getAltitude(self):
        return self.altitude
    
    def setDeparture(self, string):
        self.departure = string
        return self.departure
    
    def setDestination(self, string):
        self.destination = string
        return self.destination
    
    def getDeparture(self):
        return self.departure
    
    def getDestination(self):
        return self.destination
    
    def __str__(self):
        return f"Aeroplane({self.departure}, {self.destination})"
    

def testPlane():
    plane = Aeroplane(" ", " ")

    departure = input("please enter departure here: ")
    destination = input("please enter destination: ")

    plane.setDeparture(departure)
    plane.setDestination(destination)
    print("The departure is", plane.getDeparture(), "and destination is", plane.getDestination())

    plane.setFuel(150000)
    print("The fuel of plane is", plane.getFuel())

    plane.increaseAltitude(10000)
    print("current altitude is", plane.getAltitude())

    plane.decreaseAltitude(500)
    print("new altitude is", plane.getAltitude())


testPlane()