from cv2 import cv2
import  cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay1 = cv2.imread('hair/basic hair.png', cv2.IMREAD_UNCHANGED)
overlay2 = cv2.imread('glasses/sunglass.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)

        overlay1_resize = cv2.resize(overlay1, (int(w*1.3), int(h*0.5)))
        frame = cvzone.overlayPNG(frame, overlay1_resize, [x - 20, y - 40])

        overlay2_resize = cv2.resize(overlay2, (int(w * 1), int(h * 1)))
        frame= cvzone.overlayPNG(frame, overlay2_resize, [x - 0, y - 15])


    cv2.imshow('Snap Dude', frame)
    if cv2.waitKey(10) == ord('q'):
        break