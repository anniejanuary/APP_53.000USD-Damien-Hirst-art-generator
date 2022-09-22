import random
import turtle
from turtle import Turtle, Screen
from random import randint

new_turtle = Turtle()
screen = Screen()
turtle.colormode(255) # https://stackoverflow.com/questions/36668651/attributeerror-turtle-object-has-no-attribute-colormode-despite-turtle-py

def draw(x, y): # x and y - mouse position arguments passed by onclick()
    new_turtle.clear() # clear out the drawing if any
    new_turtle.reset() # reset the turtle to original position
    
    # using colorgram.py to extract colors from one of Damien Hirst's images in PyCharm
    # import colorgram
    # colors = colorgram.extract('hirst dots.png  ', 6)
    colors = (
        (228, 233, 237),
        (56, 108, 149),
        (226, 132, 55),
        (197, 145, 172),
        (234, 201, 101),
        (146, 81, 54)
    )

    y = -110  # starting y=-150 + step length=40  
    new_turtle.shape("circle")
    new_turtle.speed("fastest")
    screen.screensize(200, 200)
    new_turtle.hideturtle()
    new_turtle.pu()
    new_turtle.goto(-150, -150)
    new_turtle.setheading(0)
    for i in range(8):
        for i in range(7):
            new_turtle.color(random.choice(colors))
            new_turtle.pd()
            new_turtle.stamp()
            new_turtle.pu()
            new_turtle.fd(40)
        new_turtle.color(random.choice(colors))
        #or alternatively for a completely random color eg. in the last dot in each row:
        #new_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))          
        new_turtle.pd()
        new_turtle.stamp()
        new_turtle.pu()
        new_turtle.goto(-150, y)
        y += 40

      
def text(x, y):
    new_turtle_2 = Turtle()
    new_turtle_2.hideturtle()
    new_turtle_2.pu()
    new_turtle_2.goto(x, y)
    new_turtle_2.speed("slowest")
    new_turtle_2.color('black')
    style1 = ('Franklin Gothic Book', 15, 'bold')
    style2 = ('Franklin Gothic Book', 15)
    new_turtle_2.pd()
    new_turtle_2.write('Click anywhere', font=style1, align='center')
    new_turtle_2.pu()
    new_turtle_2.goto(x, y -30)
    new_turtle_2.pd()
    new_turtle_2.write('for a new computer generated Damien Hirst art', font=style2, align='center')
    new_turtle_2.hideturtle()


draw(-150, -110) # Draw the first time
screen.onclick(draw) ### Register function draw to the event mouse click
screen.onkey(screen.bye, "q") # Register function exit to event "q" key press 
text(-10, -230) #always on after first call of "draw" function"

screen.listen() # Begin listening to events eg. key presses and mouse clicks
screen.mainloop()
