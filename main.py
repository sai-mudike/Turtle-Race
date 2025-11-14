from turtle import Turtle,Screen


screen=Screen()

screen.setup(width=500,height=400)
colors=["red",'yellow','blue','green','orange','purple']


user_bet=screen.textinput('Make Your Bet','Which turtle will win the race? Enter a color: ')

x_pos=-235
y_pos=200

for i in range(6):
    y_pos-=55
    turtle=Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x_pos,y_pos)



screen.exitonclick()