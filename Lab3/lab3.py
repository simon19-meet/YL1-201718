import turtle

turtle.addshape("flat_800x800_075_f_u1.gif")
turtle.shape("flat_800x800_075_f_u1.gif")
turtle.speed(0)
for i in range(500):
    turtle.forward(200)
    turtle.right(50)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.pu()
    turtle.goto(0,0)
    turtle.right(0.1)
    turtle.pd()
turtle.mainloop()
