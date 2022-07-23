import numpy as np
import cv2

cap = cv2.VideoCapture(0) #0 can be replaced with any number for different cameras or a file path for a video to load

while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) #3 is an identifier for width
    height = int(cap.get(4)) #4 represents height

    image = np.zeros(frame.shape, np.uint8) #creates a numpy array with 0s
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()