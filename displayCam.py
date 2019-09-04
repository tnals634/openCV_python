import cv2
import numpy
import pytesseract
import matplotlib

cap = cv2.VideoCapture(0)

# 화면 크기 설정
cap.set(3, 1280)
cap.set(4,720)

# 파일 쓰기
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (1280, 720))

while True:

    ret, img_color = cap.read()

    if ret == False:
        continue
    
    if ret:
        img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)

        cv2.imshow("Color",img_color)

        writer.write(img_color)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()