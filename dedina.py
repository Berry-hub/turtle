import turtle, random
t = turtle.Turtle()
t.speed(3)
t.shape('turtle')

turtle.colormode(255)


def stvorec(strana):
    t.left(90)
    for i in range(4):
        t.forward(strana)
        t.right(90)
    t.forward(strana)


def trojuholnik(strana):
    t.right(30)
    for i in range(3):
        t.forward(strana)
        t.right(120)


def domcek(strana):
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.begin_fill()
    stvorec(strana)
    t.end_fill()
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.begin_fill()
    trojuholnik(strana)
    t.end_fill()
    t.penup()
    t.right(105)
    t.forward(((strana ** 2) * 2) ** 0.5)
    t. left(45)
    t.forward(30)
    t.pendown()


def ulica(pole):
    for strana in pole:
        domcek(strana)


ulica([50, 20, 80])

turtle.exitonclick()