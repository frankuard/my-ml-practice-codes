from line import *


pt1= (50,20)
pt2 = (450,340)

color = (0,0,225)
thickness = 3

cv2.rectangle(image, pt1, pt2, color, thickness)

cv2.imshow("Image Focused Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()