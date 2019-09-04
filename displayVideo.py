import cv2
import numpy
import pytesseract
import matplotlib

videoFile1 = 'C:/Users/Wolf/Practice/SampleVideo_1280x720_30mb.mp4'
cap = cv2.VideoCapture(videoFile1)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        cv2.imshow('video',frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

