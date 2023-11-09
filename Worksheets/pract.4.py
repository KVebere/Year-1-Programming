from graphics import *

import os


def studentInfo():
    course = input("What's your course? ")
    studentID = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + studentID[2:])


def personalDetails():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def readQuote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    # Change directory to the folder containing quotation.txt
    os.chdir("textFiles")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    inFile = open("quotation.txt", "r")

    # You can use `read()` to read the whole file into a single string
    content = inFile.read()
    print(content)

    # Or use `readLines()` to read all lines into a list
    # lines = inFile.readlines()
    # for line in lines:
    #     print(line[:-1])

    # Or use `readLine()` to read one line at a time
    # line = inFile.readline()
    # while line:
    #     print(line)
    #     line = inFile.readline()

    inFile.close()


def writeQuote():
    os.chdir("textFiles")
    outFile = open("myQuotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=outFile)
    print("(Matthew Poole)", file=outFile)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # outFile.write(content)

    outFile.close()
    
def personalGreeting():
    name=input("Yo, what is your name?")
    print(f"Hello{name}, nice to see you! ")
    
def formalName():
    name=str(input("Yo, what is your name? "))
    surname=str(input("Surname? "))
    print(f"{name[0]}. {surname}")
    
def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print(f"{kilos} kilos is equal to {ounces:.2f} ounces")
    
def generateEmail():
    name=input("Name: ")
    surname=str(input("Surname: "))
    year=input("Year: ")
    print(f"{surname.lower()[:4]}.{name.lower()[0]}.{year[-2:]}@myport.ac.uk")
    
def gradeTest():
    mark= int(input("Enter student grade here: "))
    grades = "FFFFCCBBAAAA"
    print(f"grade: {grades[mark]}") 

def graphicLetters():
    win = GraphWin("Letters", 500, 500)

    word = input("Word: ")

    for word in word:
        position = win.getMouse()

        text = Text(position, word)
        text.setSize(30)
        text.draw(win)

    win.mainloop()
    
            
def singASong():
    word = input("Enter your word: ")
    num_lines = int(input("How many lines? "))
    num_repeats = int(input("How many times to repeat? "))
    for i in range(num_lines):
        print(num_repeats * (word + " "))
       
            
def exchangeTable():
    exchange_rate = 1.17
    print("Pounds","|","Euros")
    print("===================")
    for i in range(20):
        pound_value = round(euros[i] * exchange_rate, 2)
        pound_string = (f"{pound_value:10.2f}")
        euro_string = (f"{euros[i]:10d}")
        print(pound_string,"|",euro_string)



def makeInitialism():
    word = input("Enter phrase here: ")
    for word in word.split(" "):
        print(word[0].capitalize(), end="")

            
def nameToNumber():
    name = input("Please enter your name: ")
    letters = list(name) 
    value = 0 
    for letter in letters:
        value += ord(letter) - ord('a') + 1 
        return value 
    
    
def fileInCaps():
    fileName=input("Please input file name: ")
    os.chdir("textFiles")
    inFile = open(fileName, "r")
    contents = inFile.read()
    contents
    print(contents.upper())
    inFile.close()

def totalSpending():
    os.chdir("textFiles")
    inFile = open("spending.txt", "r")
    contents = inFile.readlines()
    inFile.close()
    total = 0
    for content in contents:
        amount = float(content)
        total = total+amount
        print(amount)
    print("total", total)
        

def rainfallChart():
    inFile=open("textFiles/rainfall.txt", "r")
    lines=inFile.readlines()
    for line in lines:
        words=line.split()
        print(f"{words[0]:<12} {'*' * int(words[1])}")
    
    
   
def graphicalRainfallChart():
    inFile=open("textFiles/rainfall.txt", "r")
    lines=inFile.readlines()
    y=10
    win=GraphWin()
    for line in lines:
        words=line.split()
        text=Text(Point(50, y), words[0])
        rainfallBar = Rectangle(Point(100, y-5), Point(100+(2*int(words[1])), y+5))
        rainfallBar.setFill("red")
        text.draw(win)
        rainfallBar.draw(win)
        y=y+20
    inFile.close()
        
    



def rainfallInInches():
    inFile=open("textFiles/rainfall.txt", "r")
    outFile=open("textFiles/rainfallInches.txt", "w")
    lines=inFile.readlines()
    for line in lines:
        words=line.split()
        print(f"{words[0]:<12} { int(words[1])/25.4:0.2f}", file=outFile)
    inFile.close()
    outFile.close()
    
    
def wc():
    file = input("Enter file: ") + ".txt"
    inFile = open(file, "r")
    contents= inFile.readlines()
    lineCount=len(contents)
    characterCount=0
    wordCount=0
    for line in contents:
        wordList=line.split()
        characterCount=characterCount+len(line)
        wordCount=wordCount+len(wordList)
    print(f"There are {lineCount} lines, {wordCount} words and {characterCount} characters")
    

 
        



#Personal Notes/Questions
    #-What does the r or w do in open(fileName, "r")
    