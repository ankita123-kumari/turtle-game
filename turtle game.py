import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Dodge Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)

# Create the falling objects
falling_objects = []
for _ in range(5):
    obj = turtle.Turtle()
    obj.shape("circle")
    obj.color("red")
    obj.penup()
    obj.speed(0)
    obj.goto(random.randint(-280, 280), random.randint(100, 300))
    falling_objects.append(obj)

# Score
score = 0

# Display the score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Move the player
def go_left():
    x = player.xcor() - 20
    if x > -280:
        player.setx(x)

def go_right():
    x = player.xcor() + 20
    if x < 280:
        player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    for obj in falling_objects:
        # Move the object down
        obj.sety(obj.ycor() - random.randint(5, 15))

        # Check if the object is off the screen
        if obj.ycor() < -300:
            obj.goto(random.randint(-280, 280), random.randint(100, 300))
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

        # Check for collision with the player
        if player.distance(obj) < 20:
            game_is_on = False
            score_display.clear()
            score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 24, "normal"))

    time.sleep(0.02)

# Keep the window open
screen.mainloop()