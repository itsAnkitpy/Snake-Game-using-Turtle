from turtle import Screen
import random,time
from snake import Snake
from food import Food
from score import Scoreboard

# ------------------------------------------SNAKE GAME---------------------------------------------

# ------------------------------------------SCREEN SETUP-------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

# Import our classes of Snake, Food and Scoreboard
snake = Snake()
food = Food()
score = Scoreboard()

# Gameplay controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        # To generate food randomly of different coordinates
        food.refresh()
        # Increasing snake length of food consumption
        snake.extend()
        # Increasing score by 1 on each food consumption
        score.my_score()

    # Detect collision with the wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with its own tail. Used slicing here to avoid involving head square
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    



screen.exitonclick()


