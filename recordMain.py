import datetime
import cv2
import pandas
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from playsound import playsound
import threading
import time
import pyaudio
import wave
import os
from dotenv import load_dotenv
import random


def OHOHOHOHO(args):
    load_dotenv()
    audio_Loc = os.getenv("audio_Loc")
    chunk = 1024
    # open a wav format music
    f = wave.open(audio_Loc+random.choice(os.listdir(audio_Loc)), "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
    args.clear()


def main(threadList):
    first_frame = None
    # status_list = [None, None]
    # times = []
    # df = pandas.DataFrame(columns=["Start", "End"])
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_BUFFERSIZE, 15)
    vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter("./cam_video.mp4", vid_cod, 20.0, (640, 480))
    a = 1
    while True:

        a = a + 1
        check, frame = video.read()
        # status = 0
        output.write(frame)
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

        if cnts and len(threadList) == 0:
            t = threading.Thread(target=OHOHOHOHO, args=(threadList, ))
            threadList.append(t)
            threadList[0].start()

        cv2.imshow('Capturing', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    output.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    threadList = []
    main(threadList=threadList)
