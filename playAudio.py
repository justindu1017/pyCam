
import pyaudio
import wave
import os
from dotenv import load_dotenv
import random


def whyne(args):
    load_dotenv()
    whyne_Loc = os.getenv("whyne_Loc")
    chunk = 1024
    # open a wav format music
    f = wave.open(whyne_Loc+random.choice(os.listdir(whyne_Loc)), "rb")
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


def music(args):
    load_dotenv()
    musics_Loc = os.getenv("musics_Loc")
    chunk = 1024
    # open a wav format music
    f = wave.open(musics_Loc+random.choice(os.listdir(musics_Loc)), "rb")
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
