#Racing turtles

import turtle
import time

#Create a simulation that predicts what turtles will win a race
#Racerone - average turtle
#Eugene - runs 15% faster than an average turtle, but must wait .5 second before he can turn
#Blaze -retired, but runs at 40% increased speed

class RacingTurtle:

    def __init__ (self, speed, turnDelay, name): #Constructor *always include self
        self.name = name
        self.turt = turtle.Turtle()
        self.speed = speed
        self.turnDelay = 0 + turnDelay

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

eugene.turt.penup()
eugene.turt.sety(150)
eugene.turt.pendown()


def runRace(rt):
    time.clock()
    startTime = time.clock()
    #forward90
    
    #forward 100
     runForward(100,rt)

    #right 90
    rt.turnRight(90)

    #forward 100
     runForward(100,rt)

def runForward(dist, rt):
    Distance = int(dist * (1 - rt.speed/100))
    for i in range(leg1Distance):
        rt.forward()


print(runRace(eugene))
print(runRace(racerone))
print(runRace(blaze))





