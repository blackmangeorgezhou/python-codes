import turtle as t
import random

t.color('black')
t.penup()
t.goto(-300, 300)

# 黑夜背景
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(600)
    t.right(90)
t.end_fill()

# 星点
t.speed(0)
for i in range(500):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(random.uniform(0.5, 1), random.uniform(0.5, 1), random.uniform(0.5, 1))
    t.forward(1)

t.hideturtle()
# 阻止窗口闪退
t.done()
