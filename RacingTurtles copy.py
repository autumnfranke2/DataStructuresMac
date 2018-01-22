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
        self.speed = 20 * (1 + (speed/100))
        self.turnDelay = 0 + turnDelay

    def getX(self):
        return self.turt.xcor()

    def getY(self):
        return self.turt.ycor()

    def forward(self, distance):
        """ Moves the turtle forward soeed * distance""" #doc string (""")

        self.turt.forward(distance * self.speed)

    def turnRight(self, degrees):
        self.turt.right(degrees)
        time.sleep(self.turnDelay)

    def turnLeft(self, degrees):
        self.turt.left(degrees)
        time.sleep(self.turnDelay)

        
racerone = RacingTurtle( 0, 0, "Racer one")
eugene = RacingTurtle( 15, 0.05, "Eugene 'The Machine ' Topps")
blaze = RacingTurtle( 40, 0, "Blaze")

eugene.turt.penup()
eugene.turt.sety(150)
eugene.turt.pendown()

time.clock()
eugenestartTime = time.clock()

# leg 1
while (eugene.getX() < 100):
       eugene.forward(1)

#turn
eugene.turnRight(90)

# leg 2
    
while (eugene.getY() > 50):
       eugene.forward(1)

eugeneendTime = time.clock()





raceronestartTime = time.clock()


# leg 1
while (racerone.getX() < 100):
       racerone.forward(1)

#turn
racerone.turnRight(90)

# leg 2
    
while (racerone.getY() > -100):
       racerone.forward(1)



       

blazestartTime = time.clock()

# leg 1
while (blaze.getX() < 100):
       blaze.forward(1)

#turn
blaze.turnRight(90)

# leg 2
    
while (blaze.getY() > -100):
       blaze.forward(1)

blazeendTime = time.clock()




print(eugeneendTime - eugenestartTime)

print(raceronestartTime - raceroneendTime)

print(blazeendTime - blazestartTime)




