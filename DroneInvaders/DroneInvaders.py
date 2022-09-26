from turtle import Turtle, mainloop
from abc import *
import random
import math
import time
import turtle

class GenericLaserCannon(Turtle):
    shipX = 0
    
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__screen = self.getscreen()
        self.__screen.onkey(self.quit, "q")
        self.__bombType = GenericBomb
        self.__screen.onkey(self.switchToCluster, "2")
        self.__screen.onkey(self.switchToDefault, "1")

        self.getscreen().tracer(0)
        self.up()
        if "Ship.gif" not in self.getscreen().getshapes():
            self.getscreen().addshape("Ship.gif")
        self.shape("Ship.gif")
        self.getscreen().tracer(1)

    def quit(self):
        self.up()
        self.goto(0,((self.__yMax - self.__yMin)/2)-15)
        gameover = turtle.Turtle()
        gameover.up()
        gameover.hideturtle()
        gameover.getscreen().tracer(0)
        gameover.color("black")
        gameover.goto(0,((self.__yMax - self.__yMin)/2))
        gameover.down()
        gameover.setheading(180)
        gameover.begin_fill()
        gameover.forward(70)
        gameover.right(90)
        gameover.forward(50)
        gameover.right(90)
        gameover.forward(140)
        gameover.right(90)
        gameover.forward(50)
        gameover.right(90)
        gameover.forward(70)
        gameover.end_fill()
        gameover.up()
        gameover.goto(0,((self.__yMax - self.__yMin)/2))
        gameover.color("white")
        gameover.write("GAME OVER\n    Score  " + str(DroneInvaders.getScore()), align="center", font=("Deja Vu Sans Mono", 28, "bold"))
        gameover.getscreen().tracer(1)
        time.sleep(7)
        self.__screen.bye()
        turtle.TurtleScreen._RUNNING=True

    def getX(self):
        xPos, yPos = self.position()
        return xPos

    def getY(self):
        xPos, yPos = self.position()
        return yPos

    def getXMin(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getYMax(self):
        return self.__yMax

    def getScreen(self):
        return self.__screen

    def switchToCluster(self):
        self.__bombType = ClusterBomb

    def switchToDefault(self):
        self.__bombType = GenericBomb

    def getBombType(self):
        return self.__bombType

    @staticmethod
    def EndGame(screen, yMin, yMax):
        gameover = turtle.Turtle()
        gameover.getscreen().tracer(0)
        gameover.hideturtle()
        gameover.up()
        gameover.goto(0,((yMax - yMin)/2))
        gameover.down()
        gameover.setheading(180)
        gameover.begin_fill()
        gameover.forward(70)
        gameover.right(90)
        gameover.forward(50)
        gameover.right(90)
        gameover.forward(140)
        gameover.right(90)
        gameover.forward(50)
        gameover.right(90)
        gameover.forward(70)
        gameover.end_fill()
        gameover.up()
        gameover.goto(0,((yMax - yMin)/2))
        gameover.color("white")
        gameover.write("GAME OVER\n    Score  " + str(DroneInvaders.getScore()), align="center", font=("Arial", 28, "bold"))
        gameover.getscreen().tracer(1)
        time.sleep(7)
        screen.bye()
        turtle.TurtleScreen._RUNNING=True

class MovingLaserCannon(GenericLaserCannon):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__(xMin, xMax, yMin, yMax)
        self.getScreen().onkey(self.shoot, "space")
        self.getScreen().onkey(self.goLeft, "Left")
        self.getScreen().onkey(self.goRight, "Right")

    def shoot(self):
        self.getBombType()(30, self.getX(), self.getY(), 90, 15, self.getXMin(), self.getXMax(), self.getYMin(), self.getYMax())

    def goLeft(self):
        self.setheading(180)
        self.up()
        self.forward(5)
        MovingLaserCannon.shipX = MovingLaserCannon.shipX - 5
    
    def goRight(self):
        self.setheading(0)
        self.up()
        self.forward(5)
        MovingLaserCannon.shipX = MovingLaserCannon.shipX + 5

class LimitedBombsMovingLaserCannon(MovingLaserCannon):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__(xMin, xMax, yMin, yMax)
        self.__defaultBombsLeft = 5
        self.__clusterBombsLeft = 5

    def shoot(self):
        if self.getBombType() == GenericBomb:
            if self.__defaultBombsLeft > 0:
                self.getBombType()(5, self.getX(), self.getY(), 90, 15, self.getXMin(), self.getXMax(), self.getYMin(), self.getYMax())
                self.__defaultBombsLeft = self.__defaultBombsLeft - 1
                print(str(self.__defaultBombsLeft) + " Default Bombs left")
            else:
                print("No Default Bombs left")
        elif self.getBombType() == ClusterBomb:
            if self.__clusterBombsLeft > 0:
                self.getBombType()(5, self.getX(), self.getY(), 90, 15, self.getXMin(), self.getXMax(), self.getYMin(), self.getYMax())
                self.__clusterBombsLeft = self.__clusterBombsLeft - 1
                print(str(self.__clusterBombsLeft), " Cluster Bombs left")
            else:
                print("No Cluster Bombs left")
        else:
            print("No bombs left")

class ClickAimLaserCannon(GenericLaserCannon):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__(xMin, xMax, yMin, yMax)
        self.getScreen().onkey(self.shoot, "space")
        self.getScreen().onclick(self.aim)

    def aim(self, x, y):
        heading = self.towards(x,y)
        self.setheading(heading)

    def shoot(self):
        self.getBombType()(5, self.getX(), self.getY(), self.heading(), 15, self.getXMin(), self.getXMax(), self.getYMin(), self.getYMax())

class ArrowAimLaserCannon(GenericLaserCannon):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__(xMin, xMax, yMin, yMax)
        self.getScreen().onkey(self.shoot, "space")
        self.getScreen().onkey(self.aimLeft, "Left")
        self.getScreen().onkey(self.aimRight, "Right")

    def aimLeft(self):
        self.setheading(self.heading() + 5)
    
    def aimRight(self):
        self.setheading(self.heading() - 5)

    def shoot(self):
        self.getBombType()(5, self.getX(), self.getY(), self.heading(), 15, self.getXMin(), self.getXMax(), self.getYMin(), self.getYMax())


class BoundedTurtle(Turtle):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXmin(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getYMax(self):
        return self.__yMax

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def move(self):
        pass
    
class Drone(BoundedTurtle):
    droneList = []

    @staticmethod
    def getDrones():
        return [x for x in Drone.droneList if x.getAlive()]

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.__alive = True
        self.getscreen().tracer(0)
        self.up()
        if "Drone.gif" not in self.getscreen().getshapes():
            self.getscreen().addshape("Drone.gif")
        self.shape("Drone.gif")
        self.goto(random.randint(xMin - 1, xMax - 1), yMax - 20)
        self.setheading(random.randint(250, 290))
        self.getscreen().tracer(1)
        Drone.droneList = Drone.getDrones()
        Drone.droneList.append(self)
        self.getscreen().ontimer(self.move, (200 - (10 * DroneInvaders.getDifficulty())))

    def remove(self):
        self.__alive = False
        self.hideturtle()
        self.clear()

    def getX(self):
        xPos, yPos = self.position()
        return xPos

    def getY(self):
        xPos, yPos = self.position()
        return yPos
        
    def getAlive(self):
        return self.__alive

class GenericDrone(Drone):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)

    def move(self):
        if self.getAlive():
            self.forward(self.getSpeed())
            for a in Drone.getDrones():
                distance = math.sqrt((a.getX() - GenericLaserCannon.shipX)**2 + (a.getY())**2)
                if distance < 15:
                    GenericLaserCannon.EndGame(self.getscreen(), self.getYMin(), self.getYMax())
            if self.outOfBounds():
                xPos, yPos = self.position()
                if yPos < self.getYMin():
                    DroneInvaders.decScore()
                self.remove()
            else:
                self.getscreen().ontimer(self.move, (200 - (10 * DroneInvaders.getDifficulty())))

    def hit(self):
        self.remove()

class ShieldedDrone(Drone):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.__health = 100
        self.__hitNumber = 0
        self.color("white")
        self.write(str(self.__health) + "%")

    def move(self):
        self.clear()
        if self.getAlive():
            self.forward(self.getSpeed())
            self.write(str(int(self.__health)) + "%")
            for a in Drone.getDrones():
                distance = math.sqrt((a.getX() - GenericLaserCannon.shipX)**2 + (a.getY())**2)
                if distance < 15:
                    GenericLaserCannon.EndGame(self.getscreen(), self.getYMin(), self.getYMax())
            if self.outOfBounds():
                xPos, yPos = self.position()
                if yPos < self.getYMin():
                    DroneInvaders.decScore()
                self.remove()
            else:
                self.getscreen().ontimer(self.move, (200 - (10 * DroneInvaders.getDifficulty())))

    def hit(self):
        self.__hitNumber = self.__hitNumber + 1
        if self.__hitNumber >= 3:
            self.remove()
        self.__health = self.__health - (100/(self.__hitNumber * 2))

class Bomb(BoundedTurtle):
    def __init__(self, blastRadius, x, y, initHeading, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__blastRadius = blastRadius
        self.hideturtle()
        self.resizemode("user")
        self.turtlesize(blastRadius / 15)
        self.setheading(initHeading)
        self.up()
        self.goto(x,y)
        self.showturtle()
        self.getscreen().ontimer(self.move, 100)

    def move(self):
        exploded = False
        self.forward(self.getSpeed())
        for a in Drone.getDrones():
            if self.distance(a) < self.__blastRadius:
                a.hit()
                exploded = True
                if not a.getAlive():
                    DroneInvaders.incScore()
        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)
    
    def distance(self, other):
        p1 = self.position()
        p2 = other.position()
        return math.dist(p1, p2)

    def remove(self):
        self.hideturtle()

    def getX(self):
        xPos, yPos = self.position()
        return xPos

    def getY(self):
        xPos, yPos = self.position()
        return yPos

    def getXMin(self):
        return self.__xMin

    def getXMax(self):
        return self.__xMax

    def getYMin(self):
        return self.__yMin

    def getYMax(self):
        return self.__yMax

    def getBlastRadius(self):
        return self.__blastRadius

class GenericBomb(Bomb):
    def __init__(self, blastRadius, x, y, initHeading, speed, xMin, xMax, yMin, yMax):
        super().__init__(blastRadius, x, y, initHeading, speed, xMin, xMax, yMin, yMax)
        self.color("red", "red")
        self.shape("circle")

    def move(self):
        exploded = False
        self.forward(self.getSpeed())
        for a in Drone.getDrones():
            if self.distance(a) < self.getBlastRadius():
                a.hit()
                exploded = True
                if not a.getAlive():
                    DroneInvaders.incScore()
        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)

class ClusterBomb(Bomb):
    def __init__(self, blastRadius, x, y, initHeading, speed, xMin, xMax, yMin, yMax):
        super().__init__(blastRadius, x, y, initHeading, speed, xMin, xMax, yMin, yMax)
        self.color("green", "green")
        self.shape("triangle")
        self.__maxDistance = 200

    def move(self):
        self.forward(self.getSpeed())
        if math.dist((GenericLaserCannon.shipX, 0), (self.getX(), self.getY())) > self.__maxDistance:
            for i in range(10):
                self.remove()
                GenericBomb(5, self.getX(), self.getY(), random.randint(1,359), 15, self.getXMin(), self.getXMax(), self.getYMin(), self.getYMax())
        else:
            self.getscreen().ontimer(self.move, 100)

class DroneInvaders:
    __score = 0

    @staticmethod
    def incScore():
        DroneInvaders.__score = DroneInvaders.__score + 10
        
    @staticmethod
    def decScore():
        DroneInvaders.__score = DroneInvaders.__score - 10

    @staticmethod
    def getScore():
        return DroneInvaders.__score

    @staticmethod
    def getDifficulty():
        diff = -1
        for i in range(0, DroneInvaders.__score, 50):
            diff = diff + 1
        return diff

    def __init__(self, xMin, xMax, yMin, yMax, droneType):
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__droneType = droneType

    def play(self, LaserCannonType):
        self.__mainWin = LaserCannonType(self.__xMin, self.__xMax, self.__yMin, self.__yMax).getscreen()
        self.__mainWin.bgpic("Space.gif")
        self.__mainWin.setworldcoordinates(self.__xMin, self.__yMin - 10, self.__xMax, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000 - 10 * DroneInvaders.getDifficulty())
        self.__mainWin.onkey(self.reset, "r")
        self.__mainWin.listen()
        mainloop()

    def addDrone(self):
        if len(self.__droneType.getDrones()) < 7 + DroneInvaders.getDifficulty():
            self.__droneType(1, self.__xMin, self.__xMax, self.__yMin, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)

    def reset(self):
        for drone in self.__droneType.getDrones():
            drone.remove()
        DroneInvaders.__score = 0


game = DroneInvaders(-200, 200, 0, 400, ShieldedDrone)
game.play(LimitedBombsMovingLaserCannon)