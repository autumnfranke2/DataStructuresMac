#Racing turtles

from turtle import * #star allows us to not need .turtle

mack = Turtle()

#mack.forward(100)
#mack.left(30)
#mack.forward(100)

#Create a simulation that predicts what turtles will win a race
#Racerone - average turtle
#Eugene - runs 15% faster than an average turtle, but must wait .5 second before he can turn
#Blaze -retired, but runs at 40% increased speed

class RacingTurtle:

    def __inti__ (self, speed, turnDelay): #Constructor *always include self
        self.turt = Turtle()
        self.speed = 20 * (1 + (speed/100))
        self.turnDelay = 0 + turnDelay
