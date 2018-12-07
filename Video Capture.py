import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()     # Capture frame-by-frame

    # Our operations on the frame come here and it is converted to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # close the window when q is pressed
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
