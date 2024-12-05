#Justin Larsen
#11/3/24
#p4lab1a_Larsen
#Draw triangle and square with turtle

import turtle             
win = turtle.Screen()      
t = turtle.Turtle()    

#draw square
for i in range(4):
    t.forward(50)          
    t.left(90)             

t.forward(50)

#draw triangle
for i in range(3):
    t.forward(150)          
    t.left(120)            

#end
win.mainloop()             
