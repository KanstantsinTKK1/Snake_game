from snake import Snake
from food import Food
from score import Score
from turtle import Turtle, Screen
import time
bord = [(293,-293), (293,293), (-293,293), (-293,-293), (293,-293)]
numbers = ['0','1','2','3','4','5','6','7','8','9']

with open('data.txt', mode='r') as file:
    high_score_file = file.read()
    high_score_txt = ''
    for letter in high_score_file:
        if letter in numbers:
            high_score_txt += letter
    try:
        high_score_num = int(high_score_txt)
    except ValueError:
        high_score_num = 0

screen = Screen()
screen.setup(width=670, height=650)
screen.colormode(255)
screen.bgcolor(53, 56, 61)
screen.title("Snake game")
screen.tracer(0)
border = Turtle()
border.ht()
border.penup()
border.pensize(3)
border.pencolor('medium slate blue')
for position in bord:
    border.goto(position)
    border.pendown()
game_is_on = True

snake = Snake()
food = Food()
score_bord = Score()
if score_bord.high_points < high_score_num:
    score_bord.high_points = high_score_num
    score_bord.write_point()


screen.listen()
screen.onkey(fun=snake.turn_up, key='Up')
screen.onkey(fun=snake.turn_left, key='Left')
screen.onkey(fun=snake.turn_right, key='Right')
screen.onkey(fun=snake.turn_down, key='Down')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 16:
        food.refresh_food()
        snake.add_piece()
        score_bord.points += 1
        score_bord.write_point()

    if snake.head.xcor() > 291 or snake.head.xcor() < -291 or snake.head.ycor() > 291 or snake.head.ycor() < -291:
        score_bord.high_score()
        snake.reset_snake()


    for piece in snake.pieces[1::]:
        if snake.head.distance(piece) < 16:
            score_bord.high_score()
            snake.reset_snake()


screen.exitonclick()