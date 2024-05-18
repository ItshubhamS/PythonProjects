import random
import turtle
from turtle import *

neg_the_turtle = Turtle()
neg_the_turtle.shape("turtle")
neg_the_turtle.color("red")
neg_the_turtle.pensize(width=15)
neg_the_turtle.speed("fast")
turtle.colormode(255)


directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shapes(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        neg_the_turtle.forward(100)
        neg_the_turtle.right(angle)


for i in range(3, 11):
    neg_the_turtle.color(random_color())
    draw_shapes(i)


def random_walk():
    for _ in range(500):
        neg_the_turtle.forward(30)
        neg_the_turtle.color(random_color())
        neg_the_turtle.setheading(
            random.choice(directions),
        )


random_walk()
screen = Screen()
screen.exitonclick()
