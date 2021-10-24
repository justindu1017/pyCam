FROM python:3.6-buster





RUN apt-get update && apt-get install -y 

RUN pip install --upgrade pip

RUN pip install python-dotenv

RUN pip install opencv-python==4.1.2.30  

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

RUN pip install PyAudio

RUN apt-get update && apt-get install -y 

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get install --reinstall libxcb-xinerama0



WORKDIR /app



COPY . .



CMD [ "python", "recordMain.py" ]




# sudo docker run --ipc=host -it --device /dev/video0 --device /dev/snd -e DISPLAY=$DISPLAY --env QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix <ContainerID>