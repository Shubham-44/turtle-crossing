# turtle-crossing
This Turtle Crossing game, built with Python's Turtle module, has players control a turtle crossing a road while avoiding cars. The goal is to reach the finish line to level up, with car speeds increasing each level. Features include player movement, car generation, collision detection, and level progression.

**Controls**

Use the Up Arrow key to move the turtle forward.
Code Overview

**game.py**
Sets up the game screen and initializes the player, cars, and scoreboard.
Contains the main game loop to update the screen, create and move cars, and handle collisions and level progression.

**player.py**
Contains the Player class which handles the turtle's movement and position checks.

**Methods:**

up_only(): Moves the turtle up.
is_at_finish_line(): Checks if the turtle has reached the finish line.
go_to_start(): Resets the turtle's position to the start.

**cars.py**
Contains the Cars class which handles car creation, movement, and speed control.

**Methods:**

create_car(): Creates a new car at random intervals.
move_car(): Moves the cars across the screen.
increase_speed(): Increases the speed of the cars.

**scoreboard.py**
Contains the Scoreboard class which handles the display and update of the game score and levels.

**Methods:**

level_up(): Increases the level and updates the scoreboard.
game_over(): Displays the game over message.

**Game Features**

Player Movement: The turtle moves forward with the up arrow key.
Car Generation: Cars are generated at random positions and move across the screen.
Collision Detection: The game detects collisions between the turtle and cars.
Level Progression: Each successful crossing increases the level and car speed.
