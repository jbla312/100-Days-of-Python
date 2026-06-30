from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()
rgb_colors = [
    (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5),
    (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161),
    (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206),
    (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
    (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239),
    (217, 88, 51)
]
screen = Screen()
screen.colormode(255)
ROW = 10
COLUMN = 10
SPACING = 50
start_x = -((COLUMN - 1) * SPACING) // 2
start_y = -((ROW - 1) * SPACING) // 2

#   TODO REQUIREMENTS 10 X 10 ROWS OF SPOTS.
#   TODO DOTS OF SIZE 20 AND SPACED BY 50

def pick_color():
    return random.choice(rgb_colors)

def start_position(start_x, start_y):
    timmy_turtle.goto(start_x, start_y)
    return


timmy_turtle.hideturtle()
timmy_turtle.speed("fastest")
timmy_turtle.penup()
start_position(start_x, start_y)

for column in range(COLUMN):
    for _ in range(ROW):
        timmy_turtle.dot(20, pick_color())
        timmy_turtle.forward(50)
    start_y += 50
    start_position(start_x, start_y)















screen.exitonclick()