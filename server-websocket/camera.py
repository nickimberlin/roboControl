import cv2
import os
from imutils.video import VideoStream

def videoStream():
    vs = VideoStream(usePiCamera=False).start()

    # Create a directory to save the frames even though it is not used
    if not os.path.exists('photos'):
        os.makedirs('photos')

    while True:
        frame = vs.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
