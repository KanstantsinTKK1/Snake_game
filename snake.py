from turtle import Turtle, Screen

START_POSITION = [(0,0),(-20,0),(-40,0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]


    def create_snake(self):
        for coordinate in START_POSITION:
            self.new_segment(coordinate)


    def reset_snake(self):
        for segment in self.pieces:
            segment.ht()
        self.pieces.clear()
        self.create_snake()
        self.head = self.pieces[0]


    def move_snake(self):
            for num in range(len(self.pieces) - 1, 0, -1):
                new_x = self.pieces[num - 1].xcor()
                new_y = self.pieces[num - 1].ycor()
                self.pieces[num].goto(new_x, new_y)
            self.pieces[0].forward(20)


    def new_segment(self, position):
        new_piece = Turtle(shape='square')
        new_piece.penup()
        new_piece.speed('fastest')
        if position == (0, 0):
            new_piece.fillcolor(189, 11, 11)
        else:
            new_piece.fillcolor(252, 186, 3)
        new_piece.shapesize(1, 1, 3)
        new_piece.goto(position)
        self.pieces.append(new_piece)


    def add_piece(self):
        num_last_piece = len(self.pieces) - 1
        new_x = self.pieces[num_last_piece].xcor()
        new_y = self.pieces[num_last_piece].ycor()
        new_position = (new_x, new_y)
        self.new_segment(new_position)


    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.pieces[0].setheading(LEFT)


    def turn_right(self):
        if self.head.heading() != LEFT:
            self.pieces[0].setheading(RIGHT)


    def turn_down(self):
        if self.head.heading() != UP:
            self.pieces[0].setheading(DOWN)


    def turn_up(self):
        if self.head.heading() != DOWN:
            self.pieces[0].setheading(UP)