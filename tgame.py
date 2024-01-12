import random 
import turtle as t
while True:
    t.bgcolor('cyan')
    t.color('black')
    t.penup()                     #penup means turtel will move without drawing
    t.goto(400,-200)
    t.rt(270)
    t.pendown()
    t.forward(400)
    t.write('finish',font=24)             # notice font tag
    t.penup()
    t.goto(-400,100)
    t.rt(90)
    t.shape('turtle')
    t.color('red')
    t.pendown()
    a=t.clone()
    a.penup()
    a.goto(-400,-100)
    a.shape('turtle')
    a.color('green')
    a.pendown()
    
    die=[1,2,3,4,5,6]
    for i in range(30):
        if t.position()>(400,200) or t.position()==(400,200):
            z=t.clone()
            z.hideturtle()
            z.color('yellow')
            z.penup()
            z.goto(0,0)
            z.write('player 1 wins',font=75)
            z.pendown()
            break
        elif a.position()>(400,-200) or a.position()==(400,-200):
            z=t.clone()
            z.color('yellow')
            z.hideturtle()
            z.penup()
            z.goto(0,0)
            z.write('player 2 wins',font=75)
            z.pendown()
            break
        else:
            die_roll=random.choice(die)
            t.forward(30 * die_roll)
            die_roll2=random.choice(die)
            a.forward(30 * die_roll2)
    t.done()
