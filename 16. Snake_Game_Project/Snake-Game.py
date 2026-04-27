from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

## Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

## Game Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

## Keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#scoreboard.start_scoreboard()

## Game Loop
game_is_on = True

try:
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

except Turtle.Terminator:
    print("window closed")

try:
    screen.exitonclick()
except Turtle.Terminator:
    print("Turtle graphics window already closed.")
#screen.exitonclick()
