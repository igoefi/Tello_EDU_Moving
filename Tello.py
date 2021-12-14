# ПРЕДУПРЕЖДЕНИЕ - для управления дроном у вас должна быть английская раскладка клавиатуры
# Caps Lock не должен быть включён
# W - вперёд на указанное кол-во сантиметров(и остальные аналогично)
# A - влево
# S - назад
# D - вправо
# E - поворот по часовой на указанное кол-во градусов градусов
# Q - поворот против часовой на указанноекол-во градусов градусов
# 1 - быстрый запуск TELLO
# 0 - быстрая посадка
# 2 - кувырок вперёд
# 3 - кувырок назад
# 4 - кувырок налево
# 5 - кувырок направо
# p - подьём квадрокоптера на указанное кол-во см
# l - опускание квадрокоптера на указанное кол-во см.
# v - переключение скорости на указанное кол-во %
# z - завершение программы


from tello_binom import *
z = 1
a = 0
v = 0
start()
while z != 0:
    a = input()
    if a == "1":
        takeoff()
    elif a == "0":
        land()
    elif a == "w":
        v = int(input())
        forward(v)
    elif a == "s":
        v = int(input())
        backward(v)
    elif a == "d":
        v = int(input())
        right(v)
    elif a == "a":
        v = int(input())
        left(v)
    elif a == "q":
        v = int(input())
        anticlockwise(v)
    elif a == "e":
        v = int(input())
        clockwise(v)
    elif a == "2":
        flip_forward()
    elif a == "3":
        flip_backward()
    elif a == "4":
        flip_left()
    elif a == "5":
        flip_right()
    elif a == "p":
        v = int(input())
        up(v)
    elif a == "l":
        v = int(input())
        down(v)
    elif a == "con":
        start_video()
    elif a == "coff":
        stop_video()
    elif a == "b":
        get_battery()
    elif a == "z":
        z = 0
    elif a == "v":
        v = int(input())
        speed(v)