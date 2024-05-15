import random
from turtle import Turtle, Screen

neg_the_turtle = Turtle()
neg_the_turtle.shape("turtle")
neg_the_turtle.color("red")
# neg_the_turtle.pencolor("blue")

colors = ["red", "yellow", "blue", "violet", "green"]


def draw_shapes(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        neg_the_turtle.forward(100)
        neg_the_turtle.right(angle)


for i in range(3, 11):
    neg_the_turtle.pencolor(random.choice(colors))
    draw_shapes(i)
screen = Screen()
screen.exitonclick()
