#NOTA: el código muestra la cámara en vivo. 
import cv2
vcap = cv2.VideoCapture("rtsp://192.168.100.11:554/out.h264")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)