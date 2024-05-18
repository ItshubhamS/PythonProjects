from turtle import *

START_POINT = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    # Creating Snakes
    def create_snake(self):
        for position in START_POINT:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            new_segment.speed("fast")
            self.segments.append(new_segment)

    # Moving snake without laggging
    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        self.snake_head.setheading(90)

    def down(self):
        self.snake_head.setheading(270)

    def left(self):
        self.snake_head.setheading(180)

    def right(self):
        self.snake_head.setheading(360)
