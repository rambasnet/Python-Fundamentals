# use mouse to move turtle

import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")


def h1(x, y):
    tess.goto(x, y)


wn.onclick(h1)  # Wire up a click on the window.
wn.mainloop()
