import turtle as tur
import time
import random
global p1arr, p2arr, ball,delay, p1_len, p2_len, current_color, colors, p1count, p2count

current_color = 0
colors = ["red", "orange", "yellow", "green","blue","indigo","violet"]
p1_len = 6
p2_len = 6
p1count = 0
p2count = 0
p1arr = []
p2arr = []

def make_arr():
    global p1arr, p2arr, p1_len, p2len
    for x in range(0,p1_len):
        p1arr.append(tur.Turtle())
        p1arr[x].shape("square")
        p1arr[x].color("red")
        p1arr[x].penup()

    for x in range(0,p2_len):
        p2arr.append(tur.Turtle())
        p2arr[x].shape("square")
        p2arr[x].color("purple")
        p2arr[x].penup()

make_arr()
ball = tur.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()

def p1moveup():
    moveup(p1arr)
def p1movedown():
    movedown(p1arr)
def p2moveup():
    moveup(p2arr)
def p2movedown():
    movedown(p2arr)



def movedown(turtlearr):
    for tur in turtlearr:
        y = tur.ycor()
        if y > -270:
            tur.sety(tur.ycor()-20)
    else: return
def moveup(turtlearr):
    for tur in reversed(turtlearr):
        y = tur.ycor()
        if y < 270:
            tur.sety(tur.ycor()+20)
    else: return

def move_ball(ball):
    global p1arr, p2arr, delay, current_color, colors, p1count, p2count
    x = ball.xcor()
    y = ball.ycor()

    if(y+20*ball.dy > 300 or y + 20*ball.dy < -300):
        ball.dy = -ball.dy
        
    for p1 in p1arr:
        if ball.distance(p1) < 20:
            ball.dx  = -ball.dx
            p1count += 1
            delay -= 0.003
    for p2 in p2arr:
        if ball.distance(p2) < 20:
            ball.dx = -ball.dx
            p2count += 1
            delay -= 0.003
    
    ball.color(colors[current_color])
    if current_color + 1 < len(colors):
        current_color += 1
    else:current_color = 0
    ball.setx(x+10*ball.dx)
    ball.sety(y+10*ball.dy)
def resetGame():
    global delay, p1arr, p2arr, p1count, p2count
    p1count = 0
    p2count = 0
    delay = .08

    for x in range(0,p1_len):
        p1arr[x].goto(-450, 20*x)
    for x in range(0,p2_len):
        p2arr[x].goto(450, 20*x)
    ball.goto(0,0)
    ball.dx = 1
    ball.dy = 1

    

def main():
    global ball, p1_len, p2_len
    screen = tur.Screen()
    screen.tracer(0)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=1000, height=600)
    
    screen.listen()
    screen.onkeypress(p1moveup, 'w')
    screen.onkeypress(p1movedown, 's')
    screen.onkeypress(p2moveup, 'Up')
    screen.onkeypress(p2movedown, 'Down')

    resetGame()
    while True:
        screen.update()
        move_ball(ball)
        if(p1count % 1 == 0):
            p1_len -= 1
        if(p2count % 1 == 0):
            p2_len -= 1
        make_arr()
        if ball.xcor() > 500 or ball.xcor() < -500:
            resetGame()
        time.sleep(delay)

if __name__ == "__main__":
    main()