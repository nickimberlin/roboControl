from flask import Flask, render_template_string, render_template, request, Response
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

# importing Camera and Robot controls
from camera import videoStream
from robot import control_motors

_debug = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
CORS(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on_error_default
def default_error_handler(e):
    print("======================= ERROR")
    print(request.event["message"])
    print(request.event["args"])
    print("======================= ERROR")

@socketio.on('joystick1', namespace='/joystick1')
def control(message):
    data = message
    print(data)
    control_motors(data['data'])
    # forward_backward(data['data']['y'])

# @socketio.on('joystick2', namespace='/joystick2')
# def control(message):
#     data = message
#     left_right(data['data']['x'])

@app.route('/video_feed')
def video_feed():
    # return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(videoStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True, use_reloader=False)
