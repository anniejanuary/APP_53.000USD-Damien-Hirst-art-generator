from turtle import Turtle, Screen
from random import randint

new_turtle = Turtle()
turtle.colormode(255) # https://stackoverflow.com/questions/36668651/attributeerror-turtle-object-has-no-attribute-colormode-despite-turtle-py

def draw(x, y): # x, y are mouse position arguments passed by onclick()
    new_turtle.clear() # Clear out the drawing (if any)
    new_turtle.reset() # Reset the turtle to original position
    # using colorgram.py to extract colors from one of Damien Hirst's images
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
            # new_turtle.color(randint(0, 255), randint(0, 255),
            #                  randint(0, 255))  # https://www.geeksforgeeks.org/how-to-make-random-colors-in-python-turtle/
            new_turtle.color(random.choice(colors))
            new_turtle.pd()
            new_turtle.stamp()
            new_turtle.pu()
            new_turtle.fd(40)
        new_turtle.color(randint(0, 255), randint(0, 255),
                         randint(0, 255))  # https://www.geeksforgeeks.org/how-to-make-random-colors-in-python-turtle/
        new_turtle.pd()
        new_turtle.stamp()
        new_turtle.pu()
        new_turtle.left(90)
        new_turtle.fd(40)
        new_turtle.goto(-150, y)
        y += 40
        new_turtle.right(90)

draw(-150, -150) # Draw the first time

screen.onclick(draw) # Register function draw to the event mouse_click
screen.onkey(screen.bye, "q") # Register function exit to event key_press "q"

screen.listen() # Begin listening to events like key_press & mouse_clicks
screen.mainloop()

screen.exitonclick()
