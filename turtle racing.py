import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("white")

# Ask the user to choose a turtle
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? (red/blue/green/yellow): ")

# Create the race track
track = turtle.Turtle()
track.speed(0)
track.penup()
track.goto(-200, 100)
track.pendown()
for step in range(11):
    track.write(step, align='center')
    track.right(90)
    track.forward(200)
    track.backward(200)
    track.left(90)
    track.forward(40)
track.hideturtle()

# Create turtles for the race
colors = ["red", "blue", "green", "yellow"]
turtles = []

start_y = 80
for color in colors:
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(-220, start_y)
    start_y -= 40
    turtles.append(racer)

# Start the race
is_race_on = True
while is_race_on:
    for racer in turtles:
        racer.forward(random.randint(1, 10))
        if racer.xcor() > 200:  # Finish line
            is_race_on = False
            winner = racer.color()[0]
            print(f"The winner is the {winner} turtle!")
            if user_bet == winner:
                print("Congratulations! You guessed correctly!")
            else:
                print("Sorry, your guess was wrong.")

# Keep the window open
screen.mainloop()