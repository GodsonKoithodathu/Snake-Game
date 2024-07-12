from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# setting the game screen as per the required size and color :
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# created the objects from their respective classes :
snake = Snake()
food = Food()
score = ScoreBoard()

# for able to move the snake by using the desired keys :
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    # this is a time function from the time lib for creating a delay of 0.1 sec before updating the screen :
    time.sleep(0.1)
    screen.update()

    snake.move()

    # for generating random position of the food, extending the snake and for tracking of the score :
    if snake.head.distance(food) < 15:
        food.position_refresh()
        snake.extend()
        score.score_increase()

    # for stopping the game if the snake hits the wall :
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.highest_score()
        snake.restart()

    # for stopping the game if collision happens with the snake tail itself :
    # here in for loop we used a "slice" method in the "snake.segments" which eliminates the 0th index from the list:
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 15:
            score.highest_score()
            snake.restart()


screen.exitonclick()
