import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Picture Game")
screen.bgcolor("skyblue")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(5)

# Function to draw a rectangle
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw a triangle (roof)
def draw_triangle(color, x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

# Draw the grass
draw_rectangle("green", -400, -200, 800, 400)

# Draw the house base
draw_rectangle("brown", -100, -100, 200, 150)

# Draw the roof
draw_triangle("red", -120, 50, 240)

# Draw the sun
pen.penup()
pen.goto(200, 150)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()