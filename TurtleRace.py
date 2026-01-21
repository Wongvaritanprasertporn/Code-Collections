import turtle
import math

t = turtle.Turtle()                         # Create a Turtle object
turtle.setup(width=500, height=500)         # Set up the turtle window
t.penup()                                   # Set the starting position
t.goto(-250, 0)
t.pendown()

# Define the amplitude, frequency, and wavelength of the sine wave
for i in range(501):                        # Draw the sine wave
    y = 250 * math.sin(math.radians(i))     # Calculate the y-coordinate using the sine function
    t.goto(-250 + i, y)                     # Move to the next point on the curve
    
turtle.done()

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
turtle.setup(width=1000, height=1000)
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-500,20)
lance.goto(-500,-20)

for i in range(1000):
    x1 = random.randrange(1,100)
    x2 = random.randrange(1,100)
    andy.forward(x1)
    lance.forward(x2)
    if andy.position()[0] >= 1000:
        print("Andy won!")
        break
    elif lance.position()[0] >= 1000:
        print("Lance won!")
        break
        
wn.exitonclick()