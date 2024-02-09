import cv2
import os

def gen():
    cap = cv2.VideoCapture(0)  # 0 for the default camera

    # Create a directory to save the frames even though it is not used
    if not os.path.exists('photos'):
        os.makedirs('photos')

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')