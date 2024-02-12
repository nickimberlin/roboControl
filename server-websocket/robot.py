import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

# Control Both Motors
def control_motors(data):
    print(data)
    kit.motor1.throttle = data['x']
    kit.motor2.throttle = data['y']