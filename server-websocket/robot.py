import time
# import board
# from adafruit_motorkit import MotorKit

# kit = MotorKit(i2c=board.I2C())

# Move the car forward or backward
def forward_backward(data):
    # kit.motor2.throttle = data
    print( 'forward_backward >', data)

# Turn the car left or right
def left_right(data):
    # kit.motor1.throttle = data
    print( 'left_right >', data)

# # Control Both Motors
# def control_motors(data):
#     print(data)
#     kit.motor1.throttle = data['x']
#     kit.motor2.throttle = data['y']