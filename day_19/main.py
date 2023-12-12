import random
from turtle import Turtle, Screen

race_start = True
all_turtle_instances = []
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_cor = float(-120.0)
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Which turtle will win?")
# user_bet = screen.textinput(title="Which turtle will win the race?", prompt="Enter a color of the rainbow.").lower()

for color in colors:
    turtle_instance = Turtle(shape="turtle")
    turtle_instance.penup()
    turtle_instance.color(color)
    turtle_instance.goto((-235.0, float(y_cor)))
    y_cor = y_cor + 40
    all_turtle_instances.append(turtle_instance)


while race_start is True:
    for _turtle in all_turtle_instances:
        if _turtle.xcor() > 230:
            winner = _turtle.pencolor()
            race_start = False
            screen.title(f"{winner.title()} wins!")
        pacing = random.randint(a=1, b=10)
        _turtle.forward(pacing)


screen.exitonclick()
