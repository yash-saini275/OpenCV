import cv2
import numpy as np
import os

def captureFrame(filepath):
    video = cv2.VideoCapture(filepath + "\\RoseBloom.mp4")
    video.set(cv2.CAP_PROP_POS_MSEC,6000)       #set the video time to 6000ms.
    success, image = video.read()
    if success:
        cv2.imwrite(filepath + "\\frame_as_6.jpg", image)  #Save the image
    video.release()         #Close the video file

def colorTransform(filepath):
    image = cv2.imread(filepath + "\\frame_as_6.jpg")
    #np.savetxt("beforeChange.txt", image)

    # set blue and green channels to 0
    image[:, :, 0] = 0
    image[:, :, 1] = 0
    #np.savetxt("afterChange.txt", image)

    cv2.imwrite(filepath + "\\frame_as_6_red.jpg", image)
    cv2.waitKey(0)

captureFrame()
colorTransform()