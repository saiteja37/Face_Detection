from flask import Flask,render_template,Response
import cv2
app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
def gen():
    import cv2
    video = cv2.VideoCapture(0)
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while True:
        ret, frame = video.read()
        faces = face.detectMultiScale(frame, 1.3, 5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (25, 0, 255), 2)
        ret, jpg = cv2.imencode(".jpg", frame)
        fr=jpg.tobytes()

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +fr+ b'\r\n')
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
@app.route("/video")
def video():
    return Response(gen(),mimetype="multipart/x-mixed-replace;boundary=frame")

app.run(debug=True)