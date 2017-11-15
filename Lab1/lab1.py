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
turtle.goto(-100,0)
turtle.circle(50)
turtle.goto(-100,-50)
turtle.circle(50)
turtle.goto(-50,0)
turtle.circle(50)




turtle.mainloop()
