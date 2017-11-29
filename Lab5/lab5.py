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
       Turtle.__init__(self)
       self.begin_poly()
       self.pu()
       for i in range(2):
           self.fd(width)
           self.rt(90)
           self.fd(height)
           self.rt(90)
       self.end_poly()
       g = self.get_poly()
       register_shape("rectangle",g)
       self.shape("rectangle")
square1=Square(5)
square1.random_color()
rectangle=Rectangle(10,20)

#rectangle=Rectangle()
#exersice 2

class Hexagon(Turtle):
    def __init__(self,size,speed,times):
        Turtle.__init__(self)
        self.shapesize(size)
        
        self.begin_poly()
        self.pu()
        for i in range(6):
            
            self.rt(60)
            self.fd(100)
        self.end_poly()
        p = self.get_poly()
        register_shape("hexagon",p)
        self.shape("hexagon")
        #def move_hx():
        for cancer in range(times*2):
            self.fd(times)
        #def SetSpeed():
        self.speed(speed)
            
hexagon=Hexagon(1,1,10)






        



