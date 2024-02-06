import cv2
import os

# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture("rtsp://192.168.100.11:554/out.h264")

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error opening video stream")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame was captured successfully
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Check for 'q' key press to capture a photo
    if cv2.waitKey(1) == ord('q'):
        filename = "camera/image_{}.jpg".format(os.getpid())  # Use a unique filename based on process ID
        # Save the captured frame as a photo
        cv2.imwrite(filename, frame)
        print("Photo captured!")
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()