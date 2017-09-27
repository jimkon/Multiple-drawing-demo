import tkinter
from tkinter import *
import math


def rotate_point(point, deg):
    rads = math.radians(deg)
    return [point[0] * math.cos(rads) - point[1] * math.sin(rads),
            point[0] * math.sin(rads) + point[1] * math.cos(rads)]


def convert_screen_to_plain(point):
    return [point[0] - width / 2, -point[1] + height / 2]


def draw_line(point_1, point_2=[0, 0], color='red'):
    canvas.create_line(point_1[0] + width / 2,
                       -point_1[1] + height / 2,
                       point_2[0] + width / 2,
                       -point_2[1] + height / 2,
                       fill=color)


def button_1_press(event):
    x = event.x
    y = event.y
    global mouse_1_press
    mouse_1_press = convert_screen_to_plain([x, y])


def button_1_release(event):
    mouse_release = convert_screen_to_plain([event.x, event.y])
    for i in range(0, 2 * divisions):
        deg_step = 360 / (2 * divisions)
        draw_line(rotate_point(mouse_1_press, i * deg_step),
                  rotate_point(mouse_release, i * deg_step))
    return


def button_3_drag(event):
    x = event.x
    y = event.y
    point = convert_screen_to_plain([x, y])
    global mouse_3_last_point
    # print(point, mouse_3_last_point)
    if len(mouse_3_last_point) != 0:
        for i in range(0, 2 * divisions):
            deg_step = 360 / (2 * divisions)
            draw_line(rotate_point(mouse_3_last_point, i * deg_step),
                      rotate_point(point, i * deg_step))
    mouse_3_last_point = point


def button_3_release(event):
    global mouse_3_last_point
    mouse_3_last_point = []


root = Tk()
width = 600
height = 600
divisions = 10
mouse_1_press = []
mouse_3_last_point = []

canvas = Canvas(root, width=width, height=height)
canvas.bind("<Button-1>", button_1_press)
canvas.bind("<ButtonRelease-1>", button_1_release)

canvas.bind("<B3-Motion>", button_3_drag)
canvas.bind("<ButtonRelease-3>", button_3_release)

canvas.pack()

for i in range(0, 2 * divisions):
    deg_step = 360 / (2 * divisions)
    draw_line(rotate_point([-width, 0], i * deg_step),
              rotate_point([width, 0], i * deg_step),
              'blue')

root.mainloop()
