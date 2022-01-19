import turtle as t 
from random import randint, random

def draw_plant(col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t.Screen().bgcolor('pink')
draw_plant(5, 50, 'red', 0, 0)

while True:
    ranPts = randint(2,5) * 2 + 1
    ranSize = randint(10, 50) 
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    draw_plant(ranPts, ranSize, ranCol, ranX, ranY)