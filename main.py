from turtle import Turtle,Screen
from random import randint


screen=Screen()

screen.setup(width=500,height=400)
colors=["red",'yellow','blue','green','orange','purple']
x_pos=-235
y_pos=200
is_race_on=False

user_bet=screen.textinput('Make Your Bet','Which turtle will win the race? Enter a color: ')
all_turtles=[]

for i in range(6):
    y_pos-=55
    turtle=Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x_pos,y_pos)
    all_turtles.append(turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            
            if user_bet==winner:
                print(f"You have won")
            else:
                print(f"{winner.capitalize()} Turle is won, You Lost")

        new_distance=randint(0,10)
        turtle.forward(new_distance)



screen.exitonclick()