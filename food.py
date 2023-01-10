import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        food_color = self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if food_color == (255, 255, 255):
            self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.goto(random.randint(-260, 260), random.randint(-260, 260))
