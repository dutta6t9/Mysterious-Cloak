from flask import Flask, render_template, Response
import cv2
import numpy as np
import time

app = Flask(__name__)

def invisibility_cloak():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('invisibility_cloak.avi', fourcc, 20.0, (640, 480))
    time.sleep(2)
    background = 0  # capturing background
    for i in range(30):
        ret, background = cap.read()  # capturing image
    while (cap.isOpened()):
        ret, img = cap.read()

        if not ret:
            break

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask1 = mask1 + mask2  # OR
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)

        mask2 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

        mask2 = cv2.bitwise_not(mask1)

        res1 = cv2.bitwise_and(background, background, mask=mask1)
        res2 = cv2.bitwise_and(img, img, mask=mask2)

        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

        ret, buffer = cv2.imencode('.jpg', final_output)
        final_output = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + final_output + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(invisibility_cloak(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
