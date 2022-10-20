import cv2

#อ่านภาพ
cap = cv2.VideoCapture("image/Mark.mp4")
#cap = cv2.VideoCapture(0)

#อ่านไฟล์สำหรับ classification
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

#แสดงผลวิดีโอ
while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #จำแนกดวงตา
        face_detect = eye_cascade.detectMultiScale(gray_img,1.25,5)
        #แสดงตำแหน่งที่เจอดวงตา
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow("Output",frame)

        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()