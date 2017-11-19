print("problem 1:")
#print("Simon Deeb")
name="Simon Deeb "
print(name*100)

print("problem 2:")
#part 1
number1=10
print(number1)
#part 2
number2=number1/2
print(number2)

print("problem 3:")
list1=[3,4,8]
for item in list1:
    print (item)
    print (item*2)
total=0
for item in list1:
    total+=item
print(total)

print("problem 4:")
import turtle
#turtle.goto(100,100)
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.reset()
#help(turtle.begin_fill())
#turtle.circle(50)
#turtle.penup()

turtle.pensize(7)
turtle.color("blue")
turtle.penup()
turtle.goto(-200, -25)
turtle.pendown()
turtle.circle(90)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(90)

turtle.color("red")
turtle.penup()
turtle.goto(200, -25)
turtle.pendown()
turtle.circle(90)

turtle.color("yellow")
turtle.penup()
turtle.goto(-100, -110)
turtle.pendown()
turtle.circle(90)

turtle.color("green")
turtle.penup()
turtle.goto(100, -110)
turtle.pendown()
turtle.circle(90)





turtle.mainloop()
