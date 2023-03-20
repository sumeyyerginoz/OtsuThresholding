
import cv2
import numpy as np

image = cv2.imread("boat.jpg") # read the image

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert the image from BGR format (3 channels: Blue, Green, Red) to single-channel gray format

#Simple thresholding

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#Otsu thresholding ---- the threshold value is automatically determined by the algorithm itself

_, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # we add "binary" to get a binary imagewe want the algorithm to find the threshold value in this range instead of specifying a fixed threshold value

cv2.imshow('Original Image', image)

cv2.imshow('Grayscale Image', img)

cv2.imshow('Simple Threshold', thresh)

cv2.imshow('Otsu Threshold', thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows() # close all windows created by the program

