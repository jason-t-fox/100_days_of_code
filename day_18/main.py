from turtle import Turtle, Screen
import challenges as ch  # moving challenges over to functions

# turtle setup
turtle_guy = Turtle()
turtle_guy.shape("classic")
turtle_guy.color("blue")

# ch.challenge1(turtle_guy, size=100)
ch.spirograph(turtle_guy, 93)


screen = Screen()
screen.exitonclick()
