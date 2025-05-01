import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# img = cv.imread("Photos/cat.jpg")
# cv.imshow("Cat", img)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow("Green", blank)
#
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow("Red Square", blank)

# 2. Draw a rectangle
width = blank.shape[1] // 2
height = blank.shape[0] // 2
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness = 2)
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness = 2)
cv.rectangle(blank, (250, 0), (500, 500), (0, 0, 255), thickness = cv.FILLED)
cv.rectangle(blank, (50, 0), (250, 250), (255, 0, 0), thickness = -1)
cv.rectangle(blank, (width, height), (width + 50, height + 50), (155, 100, 100), thickness = -1)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
orange = (80, 120, 255)
cv.circle(blank, (width, height), 40, orange, thickness = -1)
cv.imshow("Circle", blank)

# 4. Draw a line
half = (width, height)
white = (255, 255, 255)
cv.line(blank, (0, 0), half, white, thickness = 3)
cv.line(blank, (100, height), (300, 400), white, thickness = 3)
cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, "Hello", (225, 225), cv.FONT_HERSHEY_TRIPLEX, 3.0, orange, 2)
cv.imshow("Text", blank)

cv.waitKey(0)