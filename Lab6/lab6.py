from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
ball1=Ball(50,"green",0.1)
ball2=Ball(30,"blue",0.1)

def check_collision(ball1,ball2):
    if ball1.radius+ball2.radius>=math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2)):
        ball1.color("red")
        ball2.fd(50)

check_collision(ball1,ball2)
circles =[ball1,ball2]
##for i in circles:
##    if i.radius+(i+1).radius>=math.sqrt(math.pow(i.xcor()-(i+1).xcor(),2)+math.pow(i.ycor()-(i+1).ycor(),2)):
##        if i.radius > (i+1).radius

