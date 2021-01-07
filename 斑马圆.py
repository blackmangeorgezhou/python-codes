import turtle as t

for i in range(100, 1, -10):
    if i % 20 == 0:
        t.fillcolor('white')
    else:
        t.fillcolor('black')
    
    t.begin_fill()
    t.circle(i*1.5, 360)
    t.end_fill()

t.hideturtle()
t.done()