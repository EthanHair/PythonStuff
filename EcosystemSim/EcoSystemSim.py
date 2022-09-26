import turtle
import random
import math

def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

def drawCircle(myTurtle, radius):
    circumference = 2 * math.pi * radius
    sideLength = circumference / 360
    drawPolygon(myTurtle, sideLength, 360)

class World:
    def __init__(self, mX, mY):
        self.__maxX = mX
        self.__maxY = mY
        self.__thingList = []
        self.__grid = []
        for aRow in range(self.__maxY):
            row = []
            for aCol in range(self.__maxX):
                row.append(None)
            self.__grid.append(row)

        self.__bearCount = 0
        self.__fishCount = 0

        if self.__maxX >= self.__maxY:
            self.__D = self.__maxY
        else:
            self.__D = self.__maxX

        self.__wTurtle = turtle.Turtle()
        self.__wScreen = turtle.Screen()
        self.__wScreen.setworldcoordinates(0,0, self.__maxX - 1, self.__maxY - 1)
        self.__wScreen.addshape("Bear2.gif")
        self.__wScreen.addshape("Fish.gif")
        self.__wScreen.addshape("Plant2.gif")
        self.__wScreen.addshape("Berry.gif")
        self.__wScreen.addshape("Alligator.gif")
        self.__wScreen.addshape("Blood.gif")
        self.__wTurtle.hideturtle()

    def draw(self):
        self.__wScreen.tracer(0)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxX - 1)
        self.__wTurtle.left(90)
        self.__wTurtle.forward(self.__maxY - 1)
        self.__wTurtle.left(90)
        for i in range(self.__maxY - 1):
            self.__wTurtle.forward(self.__maxX - 1)
            self.__wTurtle.backward(self.__maxX - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
        self.__wTurtle.forward(1)
        self.__wTurtle.right(90)
        for i in range(self.__maxX - 2):
            self.__wTurtle.forward(self.__maxY - 1)
            self.__wTurtle.backward(self.__maxY - 1)
            self.__wTurtle.left(90)
            self.__wTurtle.forward(1)
            self.__wTurtle.right(90)
        self.__wScreen.tracer(1)
        
        self.__wScreen.tracer(2)
        self.__wTurtle.up()
        self.__wTurtle.color("green")
        self.__wTurtle.begin_fill()
        self.__wTurtle.goto(-1, -1)
        self.__wTurtle.down()
        self.__wTurtle.goto(-1, self.__maxY-1)
        self.__wTurtle.goto(self.__maxX-1, self.__maxY-1)
        self.__wTurtle.goto(self.__maxX-1, -1)
        self.__wTurtle.goto(-1, -1)
        self.__wTurtle.end_fill()
        self.__wTurtle.up()
        self.__wTurtle.color("blue")
        self.__wTurtle.begin_fill()
        self.__wTurtle.goto((self.__D), 0)
        self.__wTurtle.down()
        drawCircle(self.__wTurtle, (self.__D))
        self.__wTurtle.end_fill()
        self.__wTurtle.up()
        self.__wTurtle.color("green")
        self.__wTurtle.begin_fill()
        self.__wTurtle.goto(((1/2) * self.__D), 0)
        self.__wTurtle.down()
        drawCircle(self.__wTurtle, ((1/2) * self.__D))
        self.__wTurtle.end_fill()
        self.__wScreen.tracer(3)

    def addThing(self, aThing, x, y):
        if isinstance(aThing, Bear):
            self.incBears()
        elif isinstance(aThing, Fish):
            self.incFish()
        aThing.setX(x)
        aThing.setY(y)
        self.__grid[y][x] = aThing
        aThing.setWorld(self)
        self.__thingList.append(aThing)
        aThing.appear()

    def delThing(self, aThing):
        aThing.hide()
        self.__grid[aThing.getY()][aThing.getX()] = None
        self.__thingList.remove(aThing)
        if isinstance(aThing, Bear):
            self.decBears()
        elif isinstance(aThing, Fish):
            self.decFish()

    def moveThing(self, oldX, oldY, newX, newY):
        self.__grid[newY][newX] = self.__grid[oldY][oldX]
        self.__grid[oldY][oldX] = None

    def getMaxX(self):
        return self.__maxX

    def getMaxY(self):
        return self.__maxY

    def liveALittle(self):
        if self.__thingList != [ ]:
            random.shuffle(self.__thingList)
            for aThing in self.__thingList:
                aThing.liveALittle()

    def emptyLocation(self, x, y):
        if self.__grid[y][x] == None:
            return True
        else:
            return False

    def lookAtLocation(self, x, y):
        return self.__grid[y][x]

    def freezeWorld(self):
        self.__wScreen.exitonclick()

    def getLocationType(self, x, y):
        dist = math.sqrt((x)**2 + (y)**2)
        if dist < (self.__D) and dist > ((1/2) * self.__D):
            locationType = "Water"
        else:
            locationType = "Land"
        return locationType

    def getNumBears(self):
        return self.__bearCount

    def getNumFish(self):
        return self.__fishCount

    def incBears(self):
        self.__bearCount = self.__bearCount + 1

    def decBears(self):
        self.__bearCount = self.__bearCount - 1

    def incFish(self):
        self.__fishCount = self.__fishCount + 1

    def decFish(self):
        self.__fishCount = self.__fishCount - 1

    def showCounts(self):
        self.__wTurtle.up()
        self.__wTurtle.color("black")
        self.__wTurtle.goto(0,2)
        self.__wTurtle.write("Bear Count: " + str(self.__bearCount), font=("Helvetica", 12, "bold"))
        self.__wTurtle.goto(0,1)
        self.__wTurtle.write("Fish Count: " + str(self.__fishCount), font=("Helvetica", 12, "bold"))
    
    def causeOfEnd(self, cause):
        self.__wTurtle.up()
        self.__wTurtle.color("black")
        self.__wTurtle.goto(0,3)
        self.__wTurtle.write("Too many " + cause, font=("Helvetica", 16, "bold"))

class Animal:
    def __init__(self, shape, initialEnergy, breedNum):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        self.__turtle.shape(shape)

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__energy = initialEnergy
        self.__breedTick = 0
        self.__breedNum = breedNum

        self.__offsetList = [(-1,1), (0,1),  (1,1),
                            (-1, 0),         (1,0),
                            (-1,-1), (0,-1), (1,-1)]

    def getOffsetList(self):
        return self.__offsetList

    def setX(self, newX):
        self.__xPos = newX

    def setY(self, newY):
        self.__yPos = newY

    def getX(self):
        return self.__xPos

    def getY(self):
        return self.__yPos

    def setWorld(self, aWorld):
        self.__world = aWorld

    def getWorld(self):
        return self.__world

    def appear(self):
        self.__turtle.goto(self.__xPos, self.__yPos)
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()

    def move(self, newX, newY):
        self.__world.moveThing(self.__xPos, self.__yPos, newX, newY)
        self.__xPos = newX
        self.__yPos = newY
        self.__turtle.goto(self.__xPos, self.__yPos)

    def tryToBreed(self, childType, locationType):
        randomOffsetIndex = random.randrange(len(self.__offsetList))
        randomOffset = self.__offsetList[randomOffsetIndex]
        nextX = self.__xPos + randomOffset[0]
        nextY = self.__yPos + randomOffset[1]
        while not (0 <= nextX < self.__world.getMaxX() and 0 <= nextY < self.__world.getMaxY()):
            randomOffsetIndex = random.randrange(len(self.__offsetList))
            randomOffset = self.__offsetList[randomOffsetIndex]
            nextX = self.__xPos + randomOffset[0]
            nextY = self.__yPos + randomOffset[1]
        
        if self.__world.emptyLocation(nextX, nextY) and (self.__world.getLocationType(nextX, nextY) in locationType):
            childThing = childType
            self.__world.addThing(childThing, nextX, nextY)
            self.resetBreedTick()
            self.__energy = self.__energy - 1

    def getEnergy(self):
        return self.__energy

    def incEnergy(self):
        self.__energy = self.__energy + 1

    def decEnergy(self):
        self.__energy = self.__energy - 1

    def getBreedingNum(self):
        return self.__breedNum

    def setBreedingNum(self, newNum):
        self.__breedNum = newNum

    def getBreedTick(self):
        return self.__breedTick

    def incBreedTick(self):
        self.__breedTick = self.__breedTick + 1

    def resetBreedTick(self):
        self.__breedTick = 0
    
    def death(self):
        self.__turtle.shape("Blood.gif")
    
class Veggie:
    def __init__(self, shape, crowdNum=3, breedNum=5):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        self.__turtle.shape(shape)

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__breedTick = 0
        self.__breedNum = breedNum
        self.__crowdNum = crowdNum

        self.__offsetList = [(-1,1), (0,1),  (1,1),
                            (-1, 0),         (1,0),
                            (-1,-1), (0,-1), (1,-1)]

    def setX(self, newX):
        self.__xPos = newX

    def setY(self, newY):
        self.__yPos = newY

    def getX(self):
        return self.__xPos

    def getY(self):
        return self.__yPos

    def getOffsetList(self):
        return self.__offsetList

    def setWorld(self, aWorld):
        self.__world = aWorld

    def getWorld(self):
        return self.__world

    def appear(self):
        self.__turtle.goto(self.__xPos, self.__yPos)
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()

    def tryToBreed(self, childThing, locationType):
        randomOffsetIndex = random.randrange(len(self.__offsetList))
        randomOffset = self.__offsetList[randomOffsetIndex]
        nextX = self.__xPos + randomOffset[0]
        nextY = self.__yPos + randomOffset[1]
        while not (0 <= nextX < self.__world.getMaxX() and 0 <= nextY < self.__world.getMaxY()):
            randomOffsetIndex = random.randrange(len(self.__offsetList))
            randomOffset = self.__offsetList[randomOffsetIndex]
            nextX = self.__xPos + randomOffset[0]
            nextY = self.__yPos + randomOffset[1]
        
        if self.__world.emptyLocation(nextX, nextY) and self.__world.getLocationType(nextX, nextY) == locationType:
            childThing = childThing
            self.__world.addThing(childThing, nextX, nextY)
            self.resetBreedTick()

    def getCrowdNum(self):
        return self.__crowdNum

    def getBreedNum(self):
        return self.__breedNum

    def setBreedNum(self, newNum):
        self.__breedNum = newNum

    def getBreedTick(self):
        return self.__breedTick

    def incBreedTick(self):
        self.__breedTick = self.__breedTick + 1

    def resetBreedTick(self):
        self.__breedTick = 0

class Fish(Animal):
    def __init__(self, initialEnergy=10, breedNum=12, crowdingNum=5):
        super().__init__("Fish.gif", initialEnergy, breedNum)
        self.__crowdNum = crowdingNum

    def getCrowdingNum(self):
        return self.__crowdNum

    def liveALittle(self):
        adjFish = 0
        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0<= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), Fish):
                    adjFish = adjFish + 1

        if adjFish >= self.__crowdNum:
            self.getWorld().delThing(self)
        else:
            self.incBreedTick()
            if self.getBreedTick() >= self.getBreedingNum():
                self.tryToBreed(Fish(), "Water")

            self.tryToEat()

            if self.getEnergy() == 0:
                self.getWorld().delThing(self)
            else:
                self.tryToMove()

    def tryToMove(self):
        randomOffsetIndex = random.randrange(len(self.getOffsetList()))
        randomOffset = self.getOffsetList()[randomOffsetIndex]
        nextX = self.getX() + randomOffset[0]
        nextY = self.getY() + randomOffset[1]
        moveList = []
        while len(moveList) < 5:
            while not (0 <= nextX < self.getWorld().getMaxX() and 0 <= nextY < self.getWorld().getMaxY()):
                randomOffsetIndex = random.randrange(len(self.getOffsetList()))
                randomOffset = self.getOffsetList()[randomOffsetIndex]
                nextX = self.getX() + randomOffset[0]
                nextY = self.getY() + randomOffset[1]
            moveList.append((nextX, nextY))

        if self.getWorld().emptyLocation(moveList[0][0], moveList[0][1]) and self.getWorld().getLocationType(moveList[0][0], moveList[0][1]) == "Water":
            self.move(nextX, nextY)
            self.decEnergy()
        elif self.getWorld().emptyLocation(moveList[1][0], moveList[1][1]) and self.getWorld().getLocationType(moveList[1][0], moveList[1][1]) == "Water":
            self.move(nextX, nextY)
            self.decEnergy()
        elif self.getWorld().emptyLocation(moveList[2][0], moveList[2][1]) and self.getWorld().getLocationType(moveList[2][0], moveList[2][1]) == "Water":
            self.move(nextX, nextY)
            self.decEnergy()
        elif self.getWorld().emptyLocation(moveList[3][0], moveList[3][1]) and self.getWorld().getLocationType(moveList[3][0], moveList[3][1]) == "Water":
            self.move(nextX, nextY)
            self.decEnergy()

    def tryToEat(self):
        adjPrey = []
        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0 <= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), Plant):
                    adjPrey.append(self.getWorld().lookAtLocation(newX, newY))

        if len(adjPrey) > 0:
            randomPrey = adjPrey[random.randrange(len(adjPrey))]
            preyX = randomPrey.getX()
            preyY = randomPrey.getY()

            self.getWorld().delThing(randomPrey)
            self.move(preyX, preyY)
            self.incEnergy()

class Bear(Animal):
    def __init__(self, initialEnergy=7, breedNum=8, eatNum=1):
        super().__init__("Bear2.gif", initialEnergy, breedNum)
        self.__eatNum = eatNum

    def tryToMove(self):
        bigOffsetList = [(-3,3),  (-2,3),  (-1,3),  (0,3),  (1,3),  (2,3),  (3,3),
                         (-3,2),  (-2,2),  (-1,2),  (0,2),  (1,2),  (2,2),  (3,2),
                         (-3,1),  (-2,1),  (-1,1),  (0,1),  (1,1),  (2,1),  (3,1),
                         (-3,0),  (-2,0),  (-1, 0),         (1,0),  (2,0),  (3,0),
                         (-3,-1), (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1), (3,-1),
                         (-3,-2), (-2,-2), (-1,-2), (0,-2), (1,-2), (2,-2), (3,-2),
                         (-3,-3), (-2,-3), (-1,-3), (0,-3), (1,-3), (2,-3), (3,-3),]
        adjDict ={(-1,1): [(0,1), (-1, 0)],   (0,1): [(-1,1), (1,1)],    (1,1): [(0,1), (1,0)], 
                  (-1, 0): [(-1,1), (-1,-1)],                            (1,0): [(1,1), (1,-1)], 
                  (-1,-1): [(-1, 0), (0,-1)], (0,-1): [(-1,-1), (1,-1)], (1,-1): [(0,-1), (1,0)]}
        fishList = []
        for offset in bigOffsetList:
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0<= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), Fish):
                    fishList.append((newX, newY))
        
        if len(fishList) > 0:
            randomFishIndex = random.randrange(len(fishList))
            randomFish = fishList[randomFishIndex]
            if randomFish[0] < 0:
                xChange = 1
            elif randomFish[0] > 0:
                xChange = -1
            else:
                xChange = 0
            nextX = self.getX() + xChange
            if randomFish[1] < 0:
                yChange = 1
            elif randomFish[1] > 0:
                yChange = -1
            else:
                yChange = 0
            nextY = self.getY() + yChange       

        else:
            randomOffsetIndex = random.randrange(len(self.getOffsetList()))
            randomOffset = self.getOffsetList()[randomOffsetIndex]
            xChange = randomOffset[0]
            yChange = randomOffset[1]
            nextX = self.getX() + xChange
            nextY = self.getY() + yChange
            while not (0 <= nextX < self.getWorld().getMaxX() and 0 <= nextY < self.getWorld().getMaxY()):
                randomOffsetIndex = random.randrange(len(self.getOffsetList()))
                randomOffset = self.getOffsetList()[randomOffsetIndex]
                xChange = randomOffset[0]
                yChange = randomOffset[1]
                nextX = self.getX() + xChange
                nextY = self.getY() + yChange
        
        if (0 <= nextX < self.getWorld().getMaxX() and 0 <= nextY < self.getWorld().getMaxY()) and self.getWorld().emptyLocation(nextX, nextY) and self.getWorld().getLocationType(nextX, nextY) == "Land":
            self.move(nextX, nextY)
            self.decEnergy()
        else:
            nextX = self.getX() + adjDict[xChange, yChange][0][0]
            nextY = self.getY() + adjDict[xChange, yChange][0][1]
            if (0 <= nextX < self.getWorld().getMaxX() and 0 <= nextY < self.getWorld().getMaxY()) and self.getWorld().emptyLocation(nextX, nextY) and self.getWorld().getLocationType(nextX, nextY) == "Land":
                self.move(nextX, nextY)
                self.decEnergy()
            else:
                nextX = self.getX() + adjDict[xChange, yChange][1][0]
                nextY = self.getY() + adjDict[xChange, yChange][1][1]
                if (0 <= nextX < self.getWorld().getMaxX() and 0 <= nextY < self.getWorld().getMaxY()) and self.getWorld().emptyLocation(nextX, nextY) and self.getWorld().getLocationType(nextX, nextY) == "Land":
                    self.move(nextX, nextY)
                    self.decEnergy()

    def liveALittle(self):
        adjBear = 0
        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0<= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), Bear):
                    adjBear = adjBear + 1

        if adjBear >= 5:
            self.getWorld().delThing(self)
        else:
            self.incBreedTick()
            if self.getBreedTick() >= self.getBreedingNum():
                self.tryToBreed(Bear(), "Land")

            self.tryToEat()

            if self.getEnergy() == 0:
                self.getWorld().delThing(self)
            else:
                self.tryToMove()

    def tryToEat(self):
        adjPrey = []
        currentX = self.getX()
        currentY = self.getY()

        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0 <= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), (Fish, Berry)):
                    adjPrey.append(self.getWorld().lookAtLocation(newX, newY))

        if len(adjPrey) > 0:
            for i in range(self.__eatNum):
                randomPrey = adjPrey[random.randrange(len(adjPrey))]
                preyX = randomPrey.getX()
                preyY = randomPrey.getY()

                if isinstance(randomPrey, Fish):
                    self.getWorld().addThing(Blood(), preyX, preyY)
                self.getWorld().delThing(randomPrey)
                adjPrey.remove(randomPrey)
                self.move(preyX, preyY)
                if isinstance(randomPrey, Fish):
                    self.move(currentX, currentY) 
                self.incEnergy()
                if len(adjPrey) == 0:
                    break

class Plant(Veggie):
    def __init__(self, crowdNum = 3, breedNum = 5):
        super().__init__("Plant2.gif", crowdNum, breedNum)

    def liveALittle(self):
        adjPlant = 0
        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0<= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), Plant):
                    adjPlant = adjPlant + 1

        if adjPlant >= self.getCrowdNum():
            self.getWorld().delThing(self)
        else:
            self.incBreedTick()
            if self.getBreedTick() >= self.getBreedNum():
                self.tryToBreed(Plant(), "Water")

class Berry(Veggie):
    def __init__(self, crowdNum = 3, breedNum = 5):
        super().__init__("Berry.gif", crowdNum, breedNum)

    def liveALittle(self):
        adjBerry = 0
        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0<= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), Berry):
                    adjBerry = adjBerry + 1

        if adjBerry >= self.getCrowdNum():
            self.getWorld().delThing(self)
        else:
            self.incBreedTick()
            if self.getBreedTick() >= self.getBreedNum():
                self.tryToBreed(Berry(), "Land")


class Alligator(Animal):
    def __init__(self, initialEnergy=7, breedNum=50, eatNum=1):
        super().__init__("Alligator.gif", initialEnergy, breedNum)
        self.__eatNum = eatNum
        self.__lifetime = 100

    def tryToMove(self):
        randomOffsetIndex = random.randrange(len(self.getOffsetList()))
        randomOffset = self.getOffsetList()[randomOffsetIndex]
        nextX = self.getX() + randomOffset[0]
        nextY = self.getY() + randomOffset[1]
        moveList = []
        while len(moveList) < 5:
            while not (0 <= nextX < self.getWorld().getMaxX() and 0 <= nextY < self.getWorld().getMaxY()):
                randomOffsetIndex = random.randrange(len(self.getOffsetList()))
                randomOffset = self.getOffsetList()[randomOffsetIndex]
                nextX = self.getX() + randomOffset[0]
                nextY = self.getY() + randomOffset[1]
            moveList.append((nextX, nextY))

        if self.getWorld().emptyLocation(moveList[0][0], moveList[0][1]) and self.getWorld().getLocationType(moveList[0][0], moveList[0][1]) in "Water or Land":
            self.move(nextX, nextY)
        elif self.getWorld().emptyLocation(moveList[1][0], moveList[1][1]) and self.getWorld().getLocationType(moveList[1][0], moveList[1][1]) in "Water or Land":
            self.move(nextX, nextY)
        elif self.getWorld().emptyLocation(moveList[2][0], moveList[2][1]) and self.getWorld().getLocationType(moveList[2][0], moveList[2][1]) in "Water or Land":
            self.move(nextX, nextY)
        elif self.getWorld().emptyLocation(moveList[3][0], moveList[3][1]) and self.getWorld().getLocationType(moveList[3][0], moveList[3][1]) in "Water or Land":
            self.move(nextX, nextY)

    def liveALittle(self):
        self.incBreedTick()
        if self.getBreedTick() >= self.getBreedingNum():
            self.tryToBreed(Alligator(), "Land or Water")

        self.tryToEat()

        if self.__lifetime == 0:
            self.getWorld().delThing(self)
        else:
            self.tryToMove()
        self.__lifetime = self.__lifetime - 1

    def tryToEat(self):
        adjPrey = []
        for offset in self.getOffsetList():
            newX = self.getX() + offset[0]
            newY = self.getY() + offset[1]
            if 0 <= newX < self.getWorld().getMaxX() and 0 <= newY < self.getWorld().getMaxY():
                if (not self.getWorld().emptyLocation(newX, newY)) and isinstance(self.getWorld().lookAtLocation(newX, newY), (Fish, Bear)):
                    adjPrey.append(self.getWorld().lookAtLocation(newX, newY))
        if len(adjPrey) > 0:
            for i in range(self.__eatNum):
                randomPrey = adjPrey[random.randrange(len(adjPrey))]
                preyX = randomPrey.getX()
                preyY = randomPrey.getY()

                self.getWorld().addThing(Blood(), preyX, preyY)
                self.getWorld().delThing(randomPrey)
                adjPrey.remove(randomPrey)
                self.move(preyX, preyY)
                self.incEnergy()
                if len(adjPrey) == 0:
                    break


class Blood:
    def __init__(self, lifeLength=5):
        self.__turtle = turtle.Turtle()
        self.__turtle.up()
        self.__turtle.hideturtle()
        self.__turtle.shape("Blood.gif")

        self.__xPos = 0
        self.__yPos = 0
        self.__world = None

        self.__lifetime = 0
        self.__lifeLength = lifeLength

    def setX(self, newX):
        self.__xPos = newX

    def setY(self, newY):
        self.__yPos = newY

    def getX(self):
        return self.__xPos

    def getY(self):
        return self.__yPos

    def setWorld(self, aWorld):
        self.__world = aWorld

    def getWorld(self):
        return self.__world

    def appear(self):
        self.__turtle.goto(self.__xPos, self.__yPos)
        self.__turtle.showturtle()

    def hide(self):
        self.__turtle.hideturtle()

    def liveALittle(self):
        self.__lifetime = self.__lifetime + 1
        if self.__lifetime >= self.__lifeLength:
            self.getWorld().delThing(self)

def addNewThing(myWorld, theThing, landType):
    x = random.randrange(myWorld.getMaxX())
    y = random.randrange(myWorld.getMaxY())
    while (not myWorld.emptyLocation(x, y)) or (not myWorld.getLocationType(x, y) in landType):
        x = random.randrange(myWorld.getMaxX())
        y = random.randrange(myWorld.getMaxY())
    myWorld.addThing(theThing, x, y)

def mainSimulation(numBears, numFish, numPlants, numBerries, numAlligators, lifeTime, width, height):
    numberOfBears = numBears
    numberOfFish = numFish
    numberOfPlants = numPlants
    worldLifeTime = lifeTime
    numberOfBerries = numBerries
    numberOfAlligators = numAlligators
    worldWidth = width
    worldHeight = height

    myWorld = World(worldWidth, worldHeight)
    myWorld.draw()

    for i in range(numberOfPlants):
        newPlant = Plant()
        addNewThing(myWorld, newPlant, "Water")
    
    for i in range(numberOfFish):
        energy = random.randrange(8,13)
        crowdNum = random.randrange(2,5)
        breedNum = random.randrange(6,12)
        newFish = Fish(energy, breedNum, crowdNum)
        addNewThing(myWorld, newFish, "Water")

    for i in range(numberOfBears):
        energy = random.randrange(5,9)
        breedNum = random.randrange(8,15)
        newBear = Bear(energy, breedNum, 2)
        addNewThing(myWorld, newBear, "Land")

    for i in range(numberOfBerries):
        newBerry = Berry()
        addNewThing(myWorld, newBerry, "Land")

    for i in range(numberOfAlligators):
        energy = random.randrange(5,9)
        newAlligator = Alligator(energy, 50, 2)
        addNewThing(myWorld, newAlligator, "Land or Water")

    cause = "Time"
    for i in range(worldLifeTime):
        myWorld.liveALittle()
        if myWorld.getNumBears() > numBears + 30:
            cause = "Bears"
            break
        if myWorld.getNumFish() > numFish + 30:
            cause = "Fish"
            break

    myWorld.showCounts()
    myWorld.causeOfEnd(cause)

    myWorld.freezeWorld()


mainSimulation(10, 15, 15, 15, 3, 5000, 50, 25)