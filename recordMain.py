import cv2
from playsound import playsound
import threading
import time
import wave


def OHOHOHOHO():
    print("MOVING")
    info = wave.open('output.wav', 'r')
    frames = info.getnframes()
    rate = info.getframerate()
    duration = frames / float(rate)
    playsound("./output.wav")
    print("the duar is :", duration)
    time.sleep(duration)


first_frame = None
status_list = [None, None]
times = []
video = cv2.VideoCapture(0)

time.sleep(10)
print("startingq")
t = threading.Thread(target=OHOHOHOHO)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    th_delta = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    th_delta = cv2.dilate(th_delta, None, iterations=0)
    (cnts, _) = cv2.findContours(th_delta.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(t.is_alive())

    if cnts and not t.is_alive():
        print("WHYEN")
        time.sleep(1)
        t.start()


    cv2.imshow('Capturing', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


