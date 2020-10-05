import cv2 
import numpy as np 
import matplotlib.pyplot as plt


######### BRAINSTORM ##########
#  we start with a simple mouse countroller with opencv.
#  we can use fingers, no color-segmentation bs, and separated fingers 
#  means it's in "pointer" mode, and fingers put together
#  means we are in the "click&drag" mode.
#
#  We can get this working with Skribbl.io and no need for gestures 
#  to change colors; you just have to pinch over the color you want
#
#  From there, we can add out own gestures for shortcuts in the game
#  ex: swiping to clean to board, etc. etc