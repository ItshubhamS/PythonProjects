from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed_movement = 0.10

    def move(self):
        new_x_cord = self.xcor() + self.x_move
        new_y_cord = self.ycor() + self.y_move
        self.goto(new_x_cord, new_y_cord)

    def bounce_y(self):
        self.y_move *= -1
        self.speed_movement *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.speed_movement *= 0.9

    def right_misses(self):
        self.goto(0, 0)
        self.bounce_x()

    def misses(self):
        self.goto(0, 0)
        self.speed_movement = 0.10
        self.bounce_x()
