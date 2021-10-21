import threading
import time


def sleeper():
    time.sleep(2)
    print("fff")


def main():
    print("starting")
    
    t = threading.Thread(target = sleeper)
    print("first t is alive: ", t.is_alive())

    t.start()
    print("t is alive: ", t.is_alive())
    print("Finish")
    # t.join()
    time.sleep(3)
    print("still alive? ", t.is_alive())



def main2():
    t = threading.Thread(target = sleeper)

    t.start()
    t.start()
    t.start()
    t.start()
    t.start()
    t.start()

if __name__ == ("__main__"):
    main2()