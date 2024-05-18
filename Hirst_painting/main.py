import random
import turtle as turtle_module

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [
    (224, 230, 226),
    (160, 79, 49),
    (184, 178, 181),
    (215, 194, 150),
    (151, 178, 154),
    (33, 109, 136),
    (183, 151, 39),
    (43, 130, 89),
    (149, 175, 185),
    (145, 29, 21),
    (9, 102, 77),
    (137, 70, 82),
    (211, 87, 61),
    (162, 20, 28),
    (219, 178, 172),
    (211, 179, 183),
]
tim.setheading(225)
tim.forward(320)
tim.setheading(0)
No_of_Dots = 100
for dotCount in range(1, No_of_Dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dotCount % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
