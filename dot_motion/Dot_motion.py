import math
import tkinter

root = tkinter.Tk()
c = tkinter.Canvas(root, width=600, height=600, bg="white")

c.pack()

ball = c.create_oval(100, 100, 500, 500, fill='red')
dot = c.create_oval(485, 285, 515, 315, fill='blue')

#переменная для изменения направления и скорости
speed = 0

def motion():

    global speed
    corner = 1 + speed
    x = 300 + 200 * math.cos(corner)
    y = 300 + 200 * math.sin(corner)

    c.coords(dot, (x - 16, y - 16, x + 16, y + 16))

    # Если в speed "+" заменить на "-", то меняется напрвление шара.€

    speed -= 0.015

    if corner == 0:
        speed = 0

    root.after(12, motion)

motion()
root.mainloop()
