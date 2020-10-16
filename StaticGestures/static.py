import cv2 
import numpy as np 
import matplotlib.pyplot as plt

##### Le Plan ######
# gestures:
# 0 -> white
# 1 -> blue
# 2 -> green
# 3 -> yellow
# 4 -> red
# 5 -> black

# dataset pulled from kaggle 
# https://www.kaggle.com/niksanjp/number-of-fingers?


# train a model on these 6 numbers for classification

# dataflow:
# opencv using webcam -> RGB image -> classify -> output
# https://medium.com/analytics-vidhya/sign-language-recognition-using-cnn-and-opencv-beginner-level-72091ca35a19

# 1. get the camera working to see our hand gesture
# 2. identify the region with our hand and extract
# 3. train model with the gajjilion images from kaggle
# 4. use model to predict which class of gesture the extract cv image belongs to 


# 0. threshold kaggle images
# 1. find your hand
# 2. draw a rectangle
# 3. crop that rectangle
# 4. background subtraction
# 5. threshold

def crop_image(image, x, y, width, height):
    return image[y:y + height, x:x + width]


while True:  
    # capturing the image from webcam 
    cam_capture = cv2.VideoCapture(0)
    _, image_frame = cam_capture.read()

    # to crop required part
    im2 = crop_image(image_frame, 300,300,300,300)
    
    # convert to grayscale 
    image_grayscale = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # blurring the image   
    image_grayscale_blurred =cv2.GaussianBlur(image_grayscale, (15,15), 0)

    # resize the image to 28x28
    im3 = cv2.resize(image_grayscale_blurred, (28,28), interpolation = cv2.INTER_AREA)

    # expand the dimensions from 28x28 to 1x28x28x1
    im4 = np.resize(im3, (28, 28, 1))
    im5 = np.expand_dims(im4, axis=0)   
