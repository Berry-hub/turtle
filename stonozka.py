from turtle import penup, pendown, speed, forward, back, left, right, exitonclick
speed(3)

def centipede(n):
    """ stonozka, 'n' udava pocet parov noh """
    penup()
    left(180)
    forward(450)
    right(180)
    pendown()
    left(45)
    for i in range(4):
        forward(50)
        left(90)
    forward(50)
    right(45)
    forward(10)
    for i in range(n):
        left(60)
        back(50)
        forward(50)
        right(120)
        forward(50)
        back(50)
        left(60)
        forward(75)
    exitonclick()


centipede(10)