# code source: https://www.learnopencv.com/blob-detection-using-opencv-python-c/
# this code purely uses openCV
# this is a way to try to detect the nuceli based on shapes/colours etc
# possible to tune the parameters in a way to detect the nuclei however difficult to get right

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
im = cv2.imread("img2.png", cv2.IMREAD_GRAYSCALE)
# applying blur
im = cv2.medianBlur(im, 5)

"""
img = im
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Hough cirlces which finds objects similar to circles in image
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 2)

# draws the circles around detected areas
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# the following are all things that can be tweaked to optimise recognition
# preprocessing of image to make clearer distinctions
# average filter
kernel = np.ones((5,5),np.float32)/25
new = cv2.filter2D(im,-1,kernel)

# blur
new = cv2.blur(im, (5,5))

# median blur
new = cv2.medianBlur(im, 5)

# compares the original and processed image
plt.subplot(121),plt.imshow(im),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(new),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# uses simple blob detector
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 50
params.maxThreshold = 200
 
# Filter by Area
params.filterByArea = True
params.minArea = 300
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.8
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.05
 
# Set up the detector with default parameters
detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
