from turtle import*
#step1: draw a square

color("purple")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#and of square


#drawing a door
forward(70)
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200,200)
pendown()
color("red")
right(125)
forward(120)
right(-68)
forward(120)

#draw a  right window
penup()
goto(180,180)
pendown()
color("green")
right(33)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
#draw a  left window
penup()
goto(20,180)
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)






exitonclick()