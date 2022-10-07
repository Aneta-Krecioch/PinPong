#Simple Pong in Python 3

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating > speed up a game
#wn.exitonclick() #don't close window after the programms end 

#Score
score_a = 0
score_b = 0

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
paddle_b.color("dark green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation not element on the screen, max speed
ball.shape("square")
ball.color("dark green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("dark green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function
def paddle_a_up(): #defining a function
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y) #setting new val to y

#Keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_a_up, "w")

def paddle_a_down(): #defining a function
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y) #setting new val to y

#Keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_a_down, "s")

#Function
def paddle_b_up(): #defining a function
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y) #setting new val to y

#Keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_b_up, "Up")

def paddle_b_down(): #defining a function
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) #setting new val to y

#Keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update() #refresh window

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1 #reverse the direction
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #printing score
    
    if ball.ycor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#Paddle and ball collisions
if ((ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
    ball.setx(340)
    ball.dx *= -1

if ((ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
    ball.setx(-340)
    ball.dx *= -1

