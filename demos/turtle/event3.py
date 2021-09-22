import turtle
# run two turtles using mouse clicks

turtle.setup(400, 500)              # Determine the window size
wn = turtle.Screen()               # Get a reference to the window
wn.title("Handling mouse clicks!")  # Change the window title
wn.bgcolor("lightgreen")           # Set the background color
tess = turtle.Turtle()             # Create two turtles
tess.color("purple")
alex = turtle.Turtle()             # Move them apart
alex.color("blue")
alex.forward(100)


def handler_for_tess(x, y):
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(30)


def handler_for_alex(x, y):
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    alex.right(84)
    alex.forward(50)


tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.mainloop()
