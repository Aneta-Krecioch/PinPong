#Simple Pong in Python 3

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating > speed up a game
wn.exitonclick() #don't close window after the programms end 

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation not element on the screen, max speed
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation not element on the screen, max speed
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball


#Main game loop
while True:
    wn.update() #refresh window
    
