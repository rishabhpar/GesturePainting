import cv2 
import numpy as np 
import matplotlib.pyplot as plt


############ Le Plan ################
# 2 image streams
# RGB Stream and Depth Stream

# Depth -> find pointer finger 


# Step 0: How to read camera input (librealsense on github for the SDK)
#    https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python
# Step 1: Convert depth image to numpy array and process using thresholding
# Step 2: Get moving cursor using camera
# Step 3: Calibrate drawing frame -> only for the plane at which you draw. You CAN'T stick your finger into the plane, otherwise you mess up the geometry.
# Step 4: Using RGB and polyfit the different number of fingers to get colors (Lindia and Rish)
# Step 5: Implement gestures with a library  (Lindia and Rish)
# Step 6: Improve drawing GUI
# Step 7: Report using LaTeX


# Step 0thru3 by Nov 10
# Step 4and5 by Nov 10
# Step 6and7 starting Nov 17 til Dec 2

