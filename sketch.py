import cv2
import numpy as np
img=cv2.imread('lena.png')
cv2.imshow('lena img',img)


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Image',gray_img)


inverteted_img=255-gray_img
# cv2.imshow('Inverted Image',inverteted_img)

blured_img=cv2.GaussianBlur(inverteted_img,(21,21),0)
# cv2.imshow(' Image',blured_img)

inverting_blured_img=255-blured_img
sketch=cv2.divide(gray_img,inverting_blured_img,scale=265.0)
cv2.imshow('Sketch',sketch)




cv2.waitKey(0)
