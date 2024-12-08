from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.speed('fastest')
        self.refresh_food()



    def refresh_food(self):
        self.clear()
        random_x = random.randint(-280, 280) // 20 * 20
        random_y = random.randint(-280, 280) // 20 * 20
        self.goto(random_x, random_y)
        self.dot(16,(18, 219, 175))



