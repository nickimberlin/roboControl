# import time
# import board
# from adafruit_motorkit import MotorKit

# kit = MotorKit(i2c=board.I2C())

# # function to move the car forward
# def forward(num):
#     kit.motor2.throttle = num

# # function to move the car backward
# def backward(num):
#     kit.motor2.throttle = num

# # function to turn the car left
# def left(num):
#     kit.motor1.throttle = num
    
# # function to turn the car right
# def right(num):
#     kit.motor1.throttle = num

# # function to stop the car
# def stop():
#     kit.motor1.throttle = 0
#     kit.motor2.throttle = 0

# # Move the car forward or backward
# def forward_backward(data):
#     kit.motor2.throttle = data

# # Turn the car left or right
# def left_right(data):
#     kit.motor1.throttle = data