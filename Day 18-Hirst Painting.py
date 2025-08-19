import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45), (14, 101, 109), (188, 190, 201), (11, 112, 104), (65, 66, 58)]

tim.setheading(225)
tim.color("white")
tim.forward(300)
tim.setheading(0)
num_of_dots = 101

for dot_count in range(1, num_of_dots):
    random_color = random.choice(color_list)
    tim.dot(20, random_color)
    tim.color(random_color)
    tim.forward(10)
    tim.color("white")
    tim.forward(40)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = t.Screen()
screen.exitonclick()
