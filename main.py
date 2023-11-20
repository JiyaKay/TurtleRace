from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will you choose? Enter a color: ")
turtle_color = ["red", "blue", "yellow", "green", "orange", "pink", "purple"]
all_turtles = []

y_coordinate = -90
for color in turtle_color:
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(color)
    racer.goto(x=-230, y=y_coordinate)
    y_coordinate += 30
    all_turtles.append(racer)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() == 230:
            winner = turtle.pencolor()
            is_race_on = False
            if user_bet == winner:
                print(f"You won! The {winner} turtle is the winner.")
            else:
                print(f"You lost! The {winner} turtle is the winner.")

        turtle.forward(random.randint(1, 10))


screen.exitonclick()
