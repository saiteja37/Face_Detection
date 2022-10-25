import cv2
video=cv2.VideoCapture(0)
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret,frame=video.read()
    ret,jpg=cv2.imencode(".jpg",frame)
    faces=face.detectMultiScale(frame,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(25,0,255),2)
    cv2.imshow("teja",frame)
    yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()