import turtle as turt
import time
import random
global length, score, body, colors
delay = 0.1
score = 0
h_score = 0
length = 1

body = []
colors = ["red", "orange", "pink", "yellow", "green", "purple", "hot" "pink"]
head = turt.Turtle()
head.shape("square")
head.color(random.choice(colors))
head.penup()
head.goto(-280,280)
head.direction = "Stop"


apple = turt.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
x = random.randint(-14,14) 
y = random.randint(-14, 14)
apple.setx(x * 20)
apple.sety(y * 20)
    

pen = turt.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
def draw_scoreboard():
    pen.clear()
    pen.write("Score : {}  High Score: {}".format(score,h_score), align = "center", font = ("candara", 24, "bold"))
def updateApple():
    global score, delay, length, body, h_score, colors
    if head.distance(apple) < 20:
        length += 1
        score += 10
        x = random.randint(-14,14) 
        y = random.randint(-14, 14)
        apple.setx(x * 20)
        apple.sety(y * 20)
        if delay >= 0.0001:
            delay -= 0.005

        new_seg = turt.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color(random.choice(colors))
        new_seg.penup()
        body.append(new_seg)
        if(score > h_score):
            h_score = score
        draw_scoreboard()

def resetGame():
    global length, delay, score, body
    time.sleep(1)
    
    head = turt.Turtle()
    head.shape("square")
    head.color("green")
    head.penup()
    head.goto(-280,280)
    head.direction = "Stop"

    x = random.randint(-14,14) 
    y = random.randint(-14, 14)
    apple.setx(x * 20)
    apple.sety(y * 20)
    for i in body:
        i.goto(999,999)
    body = []
    length = 1
    score = 0
    delay = 0.1
def checksegments():
    for segment in body:
        if segment.distance(head) < 20:
            resetGame()
def moveup():
    global length
    if head.direction != "down" or length == 1:
        head.direction = "up"
def movedown():
    global length
    if head.direction != "up" or length == 1:
        head.direction = "down"
def moveleft():
    global length
    if head.direction != "right" or length == 1:
        head.direction = "left"
def moveright():
    global length
    if head.direction != "left" or length == 1:
        head.direction = "right"
def stop():
    head.direction = "stop"

def checkWalls():
    #checks out of bounds
    x = head.xcor()
    y = head.ycor()
    if x > 300 or x < -300 or y > 300 or y < -300:
        resetGame()



def move():
    global length
    #makes segments work
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x,y)
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
    #helps the snake move    
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    checksegments()
    checkWalls()
    
def main(): 
    screen = turt.Screen()
    screen.tracer(0)
    screen.title("Snake")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    
    screen.listen()
    screen.onkey(moveup, 'w')
    screen.onkey(movedown, 's')
    screen.onkey(moveleft, 'a')
    screen.onkey(moveright, 'd')
    screen.onkey(stop, 'e')
    draw_scoreboard()
    while True:
        move()
        updateApple()
        screen.update()
        time.sleep(delay)
if __name__ == "__main__":
    main()
