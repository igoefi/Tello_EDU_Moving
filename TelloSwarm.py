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
# ! - повторная команда переключения в режим принятия команд
# [ - отключение всех дронов tello от локального пространства
# ] - подключение всех дронов к локальному пространству
# r,t,y,u,i - подключение дрона 1,2,3,4,5 к локальному пространству соответсвенно


# Импорт модулей
import socket
import threading
import time
import keyboard

# IP и порт Tello(добавлять и удалять по надобности)
tello1_address = ('192.168.0.120', 8889)
tello2_address = ('192.168.0.121', 8889)
tello3_address = ('192.168.0.122', 8889)
tello4_address = ('192.168.0.123', 8889)
tello5_address = ('192.168.0.124', 8889)

# IP и порт на локальном компьютере(добавлять и удалять по надобности)
local1_address = ('', 9010)
local2_address = ('', 9011)
local3_address = ('', 9012)
local4_address = ('', 9013)
local5_address = ('', 9014)

# Создание UDP соединение(добавлять и удалять по надобности)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Бинд локального адреса и порта(добавлять и удалять по надобности)
sock1.bind(local1_address)
sock2.bind(local2_address)
sock3.bind(local3_address)
sock4.bind(local4_address)
sock5.bind(local5_address)


# Отправка сообщения для Tello
def send(message, delay):
    try:
        # (добавлять и удалять по надобности)
        sock1.sendto(message.encode(), tello1_address)
        sock2.sendto(message.encode(), tello2_address)
        sock3.sendto(message.encode(), tello3_address)
        sock4.sendto(message.encode(), tello4_address)
        sock5.sendto(message.encode(), tello5_address)\

        print("Отправка сообщения: " + message)

    except Exception as e:
        print("Ошибка отправки: " + str(e))

    time.sleep(delay)


def receive():
    while True:
        try:
            # (добавлять и удалять по надобности)
            response1, ip_address = sock1.recvfrom(128)
            response2, ip_address = sock2.recvfrom(128)
            response3, ip_address = sock3.recvfrom(128)
            response4, ip_address = sock4.recvfrom(128)
            response5, ip_address = sock5.recvfrom(128)
            print("Отправка сообщения: Tello EDU #0: " + response1.decode(encoding='utf-8'))
            print("Отправка сообщения: Tello EDU #1: " + response2.decode(encoding='utf-8'))
            print("Отправка сообщения: Tello EDU #2: " + response3.decode(encoding='utf-8'))
            print("Отправка сообщения: Tello EDU #3: " + response4.decode(encoding='utf-8'))
            print("Отправка сообщения: Tello EDU #4: " + response5.decode(encoding='utf-8'))
        except Exception as e:
            # Если произошла ошибка, то закрывает сокеты(добавлять и удалять по надобности)
            sock1.close()
            sock2.close()
            sock3.close()
            sock4.close()
            sock5.close()
            print("Error receiving: " + str(e))
            break


receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()


# перевод tello в режим команд
send("command", 3)

z = 1
a = 0
v = 0
while z != 0:
    a = input()
    if a == "1":
        send("takeoff", 8)

    if a == "0":
        send("land", 8)

    if a == "w":
        v = input()
        send("forward " + v, 4)

    if a == "s":
        v = input()
        send("back " + v, 4)

    if a == "a":
        v = input()
        send("left " + v, 4)

    if a == "d":
        v = input()
        send("right " + v, 4)

    if a == "z":
        z = 0

    if a == "p":
        v = input()
        send("up " + v, 4)

    if a == "l":
        v = input()
        send("down " + v, 4)

    if a == "q":
        v = input()
        send("ccw " + v, 4)

    if a == "e":
        v = input()
        send("cw " + v, 4)

    if a == "2":
        send("flip f", 4)

    if a == "3":
        send("flip b", 4)

    if a == "4":
        send("flip l", 4)

    if a == "5":
        send("flip r", 4)

    if a == "v":
        v = input()
        send("speed " + v, 4)

    if a == "!":
        send("command", 4)
    # -----------------Управление выбором дронов(добавлять и удалять по надобности)
    if a == "[":
        sock1.close()
        sock2.close()
        sock3.close()
        sock4.close()
        sock5.close()

    if a == "r":
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock1.bind(local1_address)

    if a == "t":
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock2.bind(local2_address)

    if a == "y":
        sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock3.bind(local3_address)

    if a == "u":
        sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock4.bind(local4_address)

    if a == "i":
        sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock5.bind(local5_address)

    if a == "]":
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock1.bind(local1_address)
        sock2.bind(local2_address)
        sock3.bind(local3_address)
        sock4.bind(local4_address)
        sock5.bind(local5_address)
    # -------------------------------------------------------------
# закрытие сокетов(добавлять и удалять по надобности)
sock1.close()
sock2.close()
sock3.close()
sock4.close()
sock5.close()