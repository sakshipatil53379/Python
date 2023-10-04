from turtle import Turtle
from random import randint

steve = Turtle()
Danny = Turtle()
Chris = Turtle()
Rick = Turtle()
Finish = Turtle()




steve.color("red")
steve.shape("turtle")
steve.penup()
steve.goto(-160,100)
steve.pendown()


Danny.color("blue")
Danny.shape("turtle")
Danny.penup()
Danny.goto(-160,70)
Danny.pendown()

Chris.color("green")
Chris.shape("turtle")
Chris.penup()
Chris.goto(-160,40)
Chris.pendown()

Rick.color("pink")
Rick.shape("turtle")
Rick.penup()
Rick.goto(-160,10)
Rick.pendown()

Finish.color("black")
Finish.shape("turtle")
Finish.penup()
Finish.goto(-10,100)
Finish.forward(90)
Finish.pendown()

for i in range(100):
    steve.forward(randint(1,6))
    Danny.forward(randint(1,6))
    Chris.forward(randint(1,6))
    Rick.forward(randint(1,6))
