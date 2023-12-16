from turtle import Turtle, Screen
import challenges as ch  # moving challenges over to functions

# turtle setup
turtle_guy = Turtle()
turtle_guy.shape("classic")
#turtle_guy.color("blue")
color_list = [(230, 230, 105), (236, 236, 107), (187, 187, 146), (236, 236, 191), (24, 24, 35), (163, 163, 124), (104, 104, 212), (207, 207, 221), (37, 37, 37), (141, 141, 113)]

# ch.challenge1(turtle_guy, size=100)
# ch.spirograph(turtle_guy, 93) # it turns out this was challenge 5 as well
# ch.challenge2(turtle_guy, size=10, iterations=)
# ch.challenge3(turtle_guy, 100)
# ch.challenge4(turtle_guy, 50)
ch.hirst_dots(turtle_guy)

screen = Screen()
screen.exitonclick()
