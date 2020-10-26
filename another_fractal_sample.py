import turtle
import turtle as trtl
t = trtl.Turtle()
  
t.speed('fastest') 
  
# turning the turtle to face upwards 
t.right(-90) 
  
# the acute angle between 
# the base and branch of the Y 
angle = 30
  
# function to plot a Y 
def y(sz, level):    
  
    if level > 0: 
        turtle.colormode(255) 
        #turtle.color(0,0,255) 
          
        # splitting the rgb range for green 
        # into equal intervals for each level 
        # setting the colour according 
        # to the current level 
        t.fillcolor(0, 255//level, 0) 
          
        # drawing the base 
        t.forward(sz) 
  
        t.right(angle) 
  
        # recursive call for 
        # the right subtree 
        y(0.8 * sz, level-1) 
          
        t.pencolor(0, 255//level, 0) 
          
        t.left( 2 * angle ) 
  
        # recursive call for 
        # the left subtree 
        y(0.8 * sz, level-1) 
          
        t.pencolor(0, 255//level, 0) 
          
        t.right(angle) 
        t.forward(-sz) 
           
          
# tree of size 80 and level 7 
y(80, 7)
wn = trtl.Screen()
wn.mainloop()