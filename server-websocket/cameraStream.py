# # Import OpenCV, socket and NumPy
# import cv2
# import numpy as np
# import time
# import os

# # Create a VideoCapture object
# cap = cv2.VideoCapture(0)

# # Check if camera opened successfully
# if (cap.isOpened() == False):
#     print("Unable to read camera feed")

# # Default resolution of the frame is obtained. The default resolution is system dependent.
# # We convert the resolutions from float to integer.
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))

# # Define the codec and create VideoWriter object.
# out = cv2.VideoWriter('record' + time.strftime("%I_%M_%S_%p") + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# # Create a directory to save the frames
# if not os.path.exists('photoFrames'):
#     os.makedirs('photoFrames')

# # Loop to capture frames
# while (True):
#     ret, frame = cap.read()
#     if ret == True:
#         # export frame value to be used an html iframe src
    
#         # Write the frame into the file 'output.avi'
#         out.write(frame)

#         # Save frame into a file ./photoFrames/ + date and clock time in 12 hr format + .jpg
#         # if the file is not saved, it will be created
#         # cv2.imwrite('photoFrames/' + time.strftime("%I_%M_%S_%p") + '.jpg', frame)

#         # Display the resulting frame
#         # cv2.imshow('frame', frame)

#         # Press Q on keyboard to stop recording
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Break the loop
#     else:
#         break

# # When everything done, release the video capture and video write objects
# cap.release()
# out.release()

# # Closes all the frames
# cv2.destroyAllWindows()
