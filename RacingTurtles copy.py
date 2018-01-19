#Racing turtles

import turtle

#mack = Turtle()
#mack.forward(100)
#mack.left(30)
#mack.forward(100)

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
        sleep(self.turnDelay)

    def turnLeft(self, degrees):
        self.turt.left(degrees)
        sleep(self.turnDelay)

        
racerone = RacingTurtle( 0, 0, "Racer one")
eugene = RacingTurtle( 15, 500, "Eugene 'The Machine ' Topps")

eugene.turt.penup()
eugene.turt.sety(50)
eugene.turt.pendown()

# leg 1
while (racerone.getX < 100):
       racerone.forward(1)

#turn
racerone.turnRight(90)

# leg 2
    
while (racerone.getY > -100):
       racerone.forward(1)



##while True:
##    
##    racerone.forward(1)
##    eugene.forward(1)
## 
##
##    if racerone.turt.xcor() > 100: 
##        print(racerone.name, "wins!")
##        break
##
##    if eugene.turt.xcor() > 100: 
##        print(eugene.name, "wins!")
##        break
        
