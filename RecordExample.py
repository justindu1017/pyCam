import cv2
# Capture video from webcam
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_BUFFERSIZE, 15)
vid_cod = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter("./cam_video.mp4", vid_cod, 20.0, (640, 480))
while(True):
    # Capture each frame of webcam video
    ret, frame = video.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)
    # Close and break the loop after pressing "x" key
    if cv2.waitKey(1) & 0XFF == ord('x'):
        break
# close the already opened camera
video.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()
