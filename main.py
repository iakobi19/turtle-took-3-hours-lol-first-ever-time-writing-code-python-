import turtle
import time

# 1. Setup the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("angry Turtle on Screen")

# 2. Setup the text (The visible one at the top)
writer = turtle.Turtle()

writer.color("green") # Gives it a different color
writer.penup()
writer.goto(0, 200)    # Positions it at the top
writer.write("I am the turtle!", align="center", font=("Arial", 16, "bold"))

# 3. Setup the turtle (The Hero at the bottom)
player = turtle.Turtle()
player.shape("turtle")  # Makes it look like a turtle
player.color("red")
player.penup()
player.goto(-10, 150)   # Positions it at the top but below the writer

time.sleep(2)  # Keeps the window open for 2 seconds