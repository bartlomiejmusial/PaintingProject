import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

colors = colorgram.extract('art.jpg', 50)
list_of_colors = []
colormode(255)

for color in colors:
    rgb = color.rgb
    list_of_colors.append((rgb.r, rgb.g, rgb.b))

print(list_of_colors)

turtle = Turtle()
turtle.shape("circle")
turtle.penup()
turtle.goto(-350, -300)
number_of_dots = 208
turtle.speed("fastest")
turtle.hideturtle()

for dots in range(1, number_of_dots):
    turtle.dot(20, choice(list_of_colors))
    turtle.forward(50)

    if dots % 16 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(800)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()


# 10x10 rows of spots
# size - 20
# space between - 50
