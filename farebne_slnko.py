import turtle as t
t.speed(0)
def slnko (velkost, farba_ciary, farba_vyplne):
    """Nakresli slnko, zadaj jeho velkost, farbu ciary a vyplne"""
    t.color(farba_ciary, farba_vyplne)
    for i in range(9):
        for j in range(4):
            t.forward(velkost)
            t.left(90)
            t.left(20)
t.begin_fill()
slnko(300, 'red', 'yellow')
t.end_fill()
t.penup()
t.left(45)
t.forward(180)
t.pendown()
def oko (polomer):
    for i in range(360):
        t.forward(polomer)
        t.left(1)
#
t.color('black', 'black')
t.begin_fill()
oko(1/3)
t.end_fill()
t.penup()
#
t.right(49)
t.forward(65)
t.pendown()
#
t.begin_fill()
oko(1/3)
t.end_fill()

t.exitonclick()
