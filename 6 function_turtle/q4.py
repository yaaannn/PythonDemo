import turtle
import random
def randomcolor():
    colorArr = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
        'F'
    ]
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0, 14)]
    return '#' + color
def star(x, y, left_angle, edge_len, color='yellow'):
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.begin_fill()
    turtle.left(left_angle)
    for _ in range(5):
        turtle.forward(edge_len)
        turtle.right(144)
    turtle.end_fill()
    turtle.left(-left_angle)
turtle.screensize(800, 600, "white")
for i in range(50):
    star(random.randint(-200, 200),
         random.randint(-200, 200),
         50,100,color=randomcolor())
turtle.done()