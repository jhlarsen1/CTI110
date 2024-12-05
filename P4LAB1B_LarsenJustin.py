#Justin Larsen
#11/3/24
#p4lab1b_Larsen
#Draw Initials with turtle

import turtle

# Set up the screen and turtle
box = turtle.Screen()
t = turtle.Turtle()
box.bgcolor("black")

#choose color and pen size
t.pensize(3)  
t.color("blue")

# Draw J
t.circle(50, -90)  
t.circle(50, 180)  
t.forward(120)     

#Draw L
t.penup()
t.right(90)
t.forward(20)
t.right(90)
t.pendown()
t.forward(169)
t.left(90)
t.forward(90)


#End
t.penup()        
t.hideturtle()   
box.mainloop()    