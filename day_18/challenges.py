import random
import turtle
import colorgram


def challenge1(internal_turtle, size):
    for corners in range(4):
        internal_turtle.forward(size)
        internal_turtle.right(90)


def spirograph(internal_turtle, size):  # having fun
    for corners in range(size):
        internal_turtle.forward(size)
        internal_turtle.right(size)


def challenge2(internal_turtle, size, iterations):  # should have a loop
    for _ in range(iterations):
        internal_turtle.forward(size)
        internal_turtle.color("white")
        internal_turtle.forward(size)
        internal_turtle.color("black")


def challenge3(internal_turtle, length):
    degrees = 360
    internal_turtle.getscreen().colormode(255)
    for corners in range(3, 10):
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        internal_turtle.pencolor(rgb)
        i = 0
        while i < corners:
            internal_turtle.right(degrees / corners)
            internal_turtle.forward(length)
            i += 1


def challenge4(internal_turtle, length_of_walk):
    internal_turtle.getscreen().colormode(255)
    internal_turtle.speed(0)
    for i in range(length_of_walk):
        for direction in range(random.randint(1, 4)):
            internal_turtle.right(90)  # this way the turtle spins, which is fun
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        internal_turtle.pencolor(rgb)
        internal_turtle.pensize(random.randint(1, 10))
        internal_turtle.forward(20)


def get_colors(internal_turtle, num_colors):
    """only used one time to extract the color_list variable in main.py"""
    colors = colorgram.extract("photo-1500964757637-c85e8a162699.jpg", num_colors)
    color_list = []
    for _ in range(num_colors):
        red = colors[_].rgb.r
        green = colors[_].rgb.r
        blue = colors[_].rgb.b
        color_tuple = (red, green, blue)
        color_list.append(color_tuple)


def hirst_dots(internal_turtle):
    internal_turtle.getscreen().colormode(255)
    internal_turtle.speed("fastest")
    internal_turtle.penup()
    internal_turtle.hideturtle()
    #color_list = [(230, 230, 105), (236, 236, 107), (187, 187, 146), (236, 236, 191), (24, 24, 35), (163, 163, 124),
    #              (104, 104, 212), (207, 207, 221), (37, 37, 37), (141, 141, 113)]
    internal_turtle.setheading(225)
    internal_turtle.forward(300)
    internal_turtle.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        internal_turtle.dot(20, rgb)
        internal_turtle.forward(50)

        if dot_count % 10 == 0:
            internal_turtle.setheading(90)
            internal_turtle.forward(50)
            internal_turtle.setheading(180)
            internal_turtle.forward(500)
            internal_turtle.setheading(0)


