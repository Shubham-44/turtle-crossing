from turtle import Screen
import time
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = Cars()
scoreboard = Scoreboard()

screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=player.up_only)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.go_to_start()
        car_manager.increase_speed()

screen.exitonclick()
