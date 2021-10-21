import threading
import time
from playsound import playsound


# def sleeper():
#     time.sleep(2)
#     print("fff")


# def main():
#     print("starting")

#     t = threading.Thread(target = sleeper)
#     print("first t is alive: ", t.is_alive())

#     t.start()
#     print("t is alive: ", t.is_alive())
#     print("Finish")
#     # t.join()
#     time.sleep(3)
#     print("still alive? ", t.is_alive())


# def tt():
#     print("YOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYOYO")
#     print("YOYOYO1")
#     print("YOYOYO2")
#     time.sleep(2)


# def main3():
#     t = threading.Thread(target=tt)
#     while True:
#         print("fff")
#         time.sleep(2)
#         t.start()
#         time.sleep(20)
#         print("start again")
#         t.start()


def main4():
    string = "96742 + 33130 ="
    if "+" in string:
        tmp = string.split("=")[0].replace(" ", "").split("+")
        print(int(tmp[0])+int(tmp[1]))
    elif "-" in string:
        tmp = string.split("-")
        print(int(tmp[0])-int(tmp[1]))
    elif "*" in string:
        tmp = string.split("*")
        print(int(tmp[0])*int(tmp[1]))
    elif "%" in string:
        tmp = string.split("%")
        print(int(tmp[0]) % int(tmp[1]))


# def main2():
#     t = threading.Thread(target = sleeper)
#     t.start()
#     t.start()
#     t.start()
#     t.start()
#     t.start()
#     t.start()
if __name__ == ("__main__"):
    main4()
