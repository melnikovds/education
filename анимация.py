import turtle as t
import math

t.setup(600, 1200)
t.bgcolor('black')
t.colormode(255)
t.speed(0)
t.hideturtle()

YELLOW = (212, 255, 0)
t.pencolor(YELLOW)

screen = t.Screen()
screen.tracer(0, 0)

RINGS = 38
FRAMES = 1500

def draw_square(size, angle, wobble):
    """рисуем квадрат, центрированный относительно (0,0) с поворотом"""
    t.penup()
    t.goto(0,0)
    t.setheading(angle)

    # смещение от центра до вершины квадрата
    t.forward(size / (2 ** 0.5))
    t.right(13 + wobble)
    t.pendown()

    for _ in range(4):
        t.forward(size)
        t.right(90 + wobble * 0.2)

def draw_frame(frame):
    """отрисовываем кадр"""
    t.clear()

    for i in range(RINGS):
        # настраиваем размер слоя
        base_size = 520 / (1 + i * 0.12)
        breathing = (
            1 + 0.1 * math.sin(
            frame * 0.03 + i * 0.4
        ))
        size = base_size * breathing

        # динамически изменяем угол поворота
        angle = frame * 2 + i * 6

        # лёгкое покачивание формы
        wobble = 2 * math.sin(
            frame * 0.02 + i * 0.5
        )

        # динамически меняем толщину линий
        width = 1 + 2.5 * (
            0.5 + 0.5 * math.sin(
                frame * 0.04 + i * 0.3
        ))
        t.pensize(width)
        t.pencolor(YELLOW)

        draw_square(size, angle, wobble)

for f in range(FRAMES):
    draw_frame(f)
    if f % 2 == 0:
        screen.update()

t.done()

