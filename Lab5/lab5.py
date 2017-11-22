from turtle import *
import random
colormode(255)
#exercise 1
class Square(Turtle):
    def __init__(self,size):

        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
        
    def random_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
        self.color(r,g,b)
        
class Rectangle(Turtle):
   def __init__(self,width,height):
       print("hi")
square1=Square(5)
square1.random_color()
#rectangle=Rectangle()
#exersice 2



