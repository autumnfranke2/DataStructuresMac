#Racing turtles

import turtle
import time

#Create a simulation that predicts what turtles will win a race
#Racerone - average turtle
#Eugene - runs 15% faster than an average turtle, but must wait .5 second before he can turn
#Blaze -retired, but runs at 40% increased speed
#Zeus the lightning racer - 50% faster turns default speed

class RacingTurtle:

    def __init__ (self, speed, turnDelay, name): #Constructor *always include self
        self.name = name
        self.turt = turtle.Turtle()
        self.speed = speed
        self.turnDelay = 0.3 + turnDelay

    def getX(self):
        return self.turt.xcor()

    def getY(self):
        return self.turt.ycor()

    def forward(self):
        self.turt.forward(1)

    def turnRight(self, degrees):
        self.turt.right(degrees)
        time.sleep(self.turnDelay)

    def turnLeft(self, degrees):
        self.turt.left(degrees)
        time.sleep(self.turnDelay)

        
racerone = RacingTurtle( 0, 0, "Racer one")
eugene = RacingTurtle( 15, 0.5, "Eugene 'The Machine ' Topps")
blaze = RacingTurtle( 40, 0, "Blaze")
zeus = RacingTurtle(0,-.15, "Zeus 'The Lightning Racer'")

eugene.turt.penup()
eugene.turt.sety(150)
eugene.turt.pendown()

raceTest = [100,90,100,-90,100]

irtlOval = [100,-90,100,-90,200,-90,100,-90,100]

commandCounter = 0

def runRace(rt , track):
    time.clock()
    startTime = time.clock()

    for distance in track:

        if commandCounter % 2 == 0:
            runForward(distance,rt)
        else:
            rt.turnRight(distance)

        commandCounter += 1
        
    
##    runForward(100,rt)
##
##    rt.turnRight(90)
##
##    runForward(100,rt)

def runForward(dist, rt):
    Distance = int(dist * (1 - rt.speed/100))
    for i in range(leg1Distance):
        rt.forward()


print(runRace(eugene,irtlOval))
print(runRace(racerone,irtlOval))
print(runRace(blaze,irtlOval))
print(runRace(zeus,irtlOval))





