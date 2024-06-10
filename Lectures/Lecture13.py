from enum import Enum

class Mood(Enum):
    HAPPY = "happy"
    SAD = "sad"
    ANNOYED = "annoyed"
    HUNGRY = "hungry"

    # @classmethod
    # def isValid(cls, mood):
    #     return mood in cls.__members__.values()

class Hamster:
    def __init__(self, name):
        self.name = name
        self.feeling = Mood.HAPPY
    
    def getFeeling(self):
        return self.feeling.value
    
    def setFeeling(self, mood):
        # if Mood.isValid(mood):
        self.feeling = mood

class HamsterEnclosure: 
    def __init__(self):
        self.hamsters = []
    
    def addHamster(self, hamster):
        self.hamsters.append(hamster)
    
    def removeHamster(self, name):
        for hamster in self.hamsters:
            if hamster.name == name:
                self.hamsters.remove(hamster)
                return 
    
    def updateFeeling(self, name, newMood):
        for hamster in self.hamsters:
            if hamster.name == name:
                hamster.setFeeling(newMood)
                return











def testHamster():
    kombo = Hamster("Kombo")
    inspector = Hamster("Inspector")

    print(kombo.getFeeling())
    # print(inspector.getFeeling())

    kombo.setFeeling(Mood.SAD)
    print(kombo.getFeeling())

testHamster()

