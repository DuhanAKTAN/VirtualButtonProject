import cv2 as cv
import mediapipe
import handTrackingModule as htm
import serial
import time

#arduino için haberleşme başlatilmasi
ser = serial.Serial("COM5",9600,timeout=1)

wCam,hCam = 600,600

#video başlatma 
cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

#yazdiğimiz module den bir obje oluşturma
detector = htm.handDetector(detectionCon=0.75)

string = ""
while True:
    success,img=cap.read()

    img = detector.findHands(img,draw=True)
    lmlist = detector.findPosition(img)

    cv.rectangle(img, (50, 25), (150, 125), (0, 255, 0),cv.FILLED)
    cv.rectangle(img, (200, 25), (300, 125), (255, 0, 0),cv.FILLED)
    cv.rectangle(img, (350, 25), (450, 125), (0, 0, 255),cv.FILLED)
    cv.rectangle(img, (500, 25), (600, 125), (0, 0, 0),cv.FILLED)


    if len(lmlist) != 0:
        x,y=lmlist[8][1],lmlist[8][2]
        if x > 50 and y> 25 and x < 150 and y < 125:
            string="green"
        elif x > 200 and y> 25 and x < 300 and y < 125:
            string="blue"
        elif x > 350 and y> 25 and x < 450 and y < 125:
            string="red"
        elif x > 500 and y> 25 and x < 600 and y < 125:
            string="black"
        

    print(string)

    #arduino ya parmak sayisini gönderme
    ser.write(f'{string}\n'.encode())
    time.sleep(0.1)

    cv.imshow("video",img)
    c=cv.waitKey(1)
    if c==27:
        break

cap.release()
cv.destroyAllWindows()
ser.close()

