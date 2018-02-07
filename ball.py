from turtle import *

class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.pu()
        self.x = x
        self.y = y
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)

    def move(self,screen_width,screen_height):
        current_x = self.xcor()
        new_x = current_x + self.dx
        current_y = self.ycor()
        new_y = current_y + self.dy
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        top_side_ball = new_y + self.r
        bottom_side_ball = new_y - self.r
        #print(new_x,new_y)
        self.goto(new_x,new_y)
        if(right_side_ball >= screen_width or left_side_ball <= -screen_width):
            self.dx= (-1)*self.dx
            self.clear()
        elif(top_side_ball >= screen_height or bottom_side_ball <= -screen_height):
            self.dy= (-1)*self.dy
            self.clear()

##b=Ball(4,4,5,5,100,"blue")
##for i in range(200):
##    print(b.pos())
##    b.move(100,100)
##c=0

##import turtle
##        
##SCREEN_WIDTH=round(turtle.getcanvas().winfo_width()/2)
##SCREEN_HEIGHT=round(turtle.getcanvas().winfo_height()/2)
##b = Ball(0,0,3,3,10,"green")
##for i in range(1000):
##    b.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    
