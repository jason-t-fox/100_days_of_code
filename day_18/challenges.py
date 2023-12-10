def challenge1(internal_turtle, size):
    for corners in range(4):
        internal_turtle.forward(size)
        internal_turtle.right(90)


def spirograph(internal_turtle, size):  # having fun
    for corners in range(size):
        internal_turtle.forward(size)
        internal_turtle.right(size)

