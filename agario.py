import turtle
import time
import random
from ball import Ball
import math


turtle.tracer(0)
turtle.hideturtle()
turtle.Screen().bgpic('turtle-under-sea-desktop-background.gif')
score=0
generate_count=1
change=1

my_color=(random.random(), random.random(), random.random())

RUNNING=True
SLEEP=0.07
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

print(SCREEN_WIDTH,SCREEN_HEIGHT)

MY_BALL=Ball(15,1,0,0,20,my_color)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 40
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALL=[]

def change_bgpic(pic):
    if pic==1:
        turtle.Screen().bgpic('cool-desktop-hd-wallpaper.gif')
    elif pic==2:
        turtle.Screen().bgpic('wallpaper-landscape-patagonia.gif')
    elif pic==3:
        turtle.Screen().bgpic('Beach-Sunset-1080p-Hd-Wallpaper-For-Desktop-HD-Pic.gif')
    else:
        turtle.Screen().bgpic('turtle-under-sea-desktop-background.gif')
def change_myball_color():
    MY_BALL.color(random.random(), random.random(), random.random())
    

def Add_Ball():
    x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS)+120, int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)-120)
    y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS)+120, int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)-120)
    dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
    radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS-20)
    color = (random.random(), random.random(), random.random())
    b=Ball(x,y,dx,dy,radius,color)
    BALL.append(b)

for i in range(NUMBER_OF_BALLS):
    Add_Ball()

def move_all_balls():
    for i in BALL:
        #print(i.r,i.dx,i.dy)
        i.move(SCREEN_WIDTH,SCREEN_HEIGHT)


def collide(ball_a,ball_b):
    if ball_a == ball_b:
        return False
    d=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    Sum=ball_a.r+ball_b.r
    if d+10<=Sum:
        return True
    return False 
def check_all_balls_collision():
    for ball_a in BALL:
        for ball_b in BALL:
            if collide(ball_a,ball_b):
                a=ball_a.r
                b=ball_b.r
                x_cor=random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS+120,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS-120)
                y_cor=random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS+120,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS-120)
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX-10)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY-10)
                radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS-20)
                color=(random.random(),random.random(),random.random())
                while(dx == 0 or dy == 0):
                    dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX-10)
                    dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY-10)
            
                if(a<b):
                    ball_a.x=x_cor
                    ball_a.y=y_cor
                    ball_a.goto(x_cor,y_cor)
                    
                    ball_a.dx=dx
                    ball_a.dy=dy
                
                    ball_a.r=radius
                    ball_a.shapesize(radius/10)
                    
                    ball_a.color(color)
                    
                    ball_b.r=ball_b.r+1
                    ball_b.shapesize(ball_b.r/10)
                
                else:
                    ball_b.x=x_cor
                    ball_b.y=y_cor
                    ball_b.goto(x_cor,y_cor)
                    
                    ball_b.dx=dx
                    ball_b.dy=dy
                
                    ball_b.r=radius
                    ball_b.shapesize(radius/10)
                    
                    ball_b.color(color)
                    
                    ball_a.r=ball_a.r+1
                    ball_a.shapesize(ball_a.r/10)



def check_myball_colision():
    global score
    for i in BALL:
        if(collide(MY_BALL,i)==True):
            #print(MY_BALL.pos(), i.pos())
            b1=i.r
            myb=MY_BALL.r
            if(b1>myb):
                return False
            score+=1
            x_cor=random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
            y_cor=random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
            dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
            dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
            radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
            color=(random.random(),random.random(),random.random())
            while(dx == 0 or dy == 0):
                dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                                 
            i.x=x_cor
            i.y=y_cor
            i.goto(x_cor,y_cor)
                    
            i.dx=dx
            i.dy=dy
                
            i.r=radius
            i.shapesize(radius/10)
                    
            i.color(color)
                    
            MY_BALL.r=MY_BALL.r+1
            MY_BALL.shapesize(MY_BALL.r/10)
            
    return True


def movearound(event):
    
    MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)
    
    #MY_BALL.goto(event.x-SCREEN_WIDTH,SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()




while RUNNING==True:
    change_myball_color()
    turtle.clear()
    turtle.color("white")
    turtle.write("Score: "+str(score),font=("David",20,"normal"),align='center')

    
    
    if MY_BALL.r>=200:
        MY_BALL.r=200
    #print(RUNNING)
    if(SCREEN_WIDTH!=int(turtle.getcanvas().winfo_width()/2) or SCREEN_HEIGHT!=int(turtle.getcanvas().winfo_height()/2)):
        SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
        SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)
    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    #print(check_myball_colision())
    RUNNING=check_myball_colision()
    #check_myball_colision()
##    c+=1
##    if(c==50):
##        RUNNING=False
##    turtle.getscreen().update()
##    time.sleep(SLEEP)

    #if score==generate_count*50:

    if score==generate_count*50:
        Add_Ball()
        generate_count+=1


    if score==change*10:
        MAXIMUM_BALL_RADIUS+=10
        change+=1
        change_bgpic(random.randint(1,5))
        
    for i in BALL:
        if i.r>=190:
            i.r=190
    
    turtle.getscreen().update()
    time.sleep(SLEEP)

turtle.Screen().bgpic('annoying_terribad.gif')


    
    #move_all_balls()

##for i in range(100):
##    move_all_balls()
##    #print(SCREEN_WIDTH,SCREEN_HEIGHT)
##    #BALL[0].move(SCREEN_WIDTH,SCREEN_HEIGHT)

    


                
##while True:ffff
##    movearound(MY_BALL)
 
        
    

        
