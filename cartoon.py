#Import liberary for operation
import cv2
import numpy as np

#Select the image for cartoonize
image = cv2.imread("Pass.png");

#process for outlining the image
fade = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fade = cv2.medianBlur(fade, 5)
outlines = cv2.adaptiveThreshold(fade, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#Converting into cartoon image
colour = cv2.bilateralFilter(image, 10, 250, 250)
cartoonImg = cv2.bitwise_and(colour, colour, mask = outlines)

#Titles
cv2.imshow("Image",image)
cv2.imshow("Outlines", outlines)
cv2.imshow("Cartoon", cartoonImg)
cv2.waitKey(0)
cv2.destroyAllWindows()