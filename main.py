import turtle as turt

t = turt.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

def Draw_circle(color, size, is_fill):
    """Draw a circle."""

    if is_fill: t.begin_fill()

    t.color(color)
    t.circle(size)
    if is_fill: t.end_fill()

t.pendown()
t.goto(0,0)
# тело
cord = (0, 0)
module = 1
while module <= 5:
    print(f"LOG: module vaul: {module}")
    t.goto(cord)
    Draw_circle('green', 20, True)
    module += 1
    cord = (cord[0], cord[1] + 40)


# усики
t.penup()
t.color("black")
t.goto(0, 200)
t.setheading(120)
t.pendown()
t.circle(50, 60)

t.penup()
t.goto(0, 200)
t.setheading(60)
t.pendown()
t.circle(-50, 60)

# внешние крылья

t.penup()
t.goto(80, 70)
t.pendown()
Draw_circle('red', 60, True)

t.penup()
t.goto(-80, 70)
t.pendown()
Draw_circle('red', 60, True)


t.penup()
t.goto(50, 10)
t.pendown()
Draw_circle('red', 30, True)

t.penup()
t.goto(-50, 10)
t.pendown()
Draw_circle('red', 30, True)

# внутренние
t.penup()
t.goto(80, 130)
t.pendown()
Draw_circle('blue', 30, True)

t.penup()
t.goto(-80, 130)
t.pendown()
Draw_circle('blue', 30, True)


t.penup()
t.goto(50, 40)
t.pendown()
Draw_circle('blue', 15, True)

t.penup()
t.goto(-50, 40)
t.pendown()
Draw_circle('blue', 15, True)




turt.done()
