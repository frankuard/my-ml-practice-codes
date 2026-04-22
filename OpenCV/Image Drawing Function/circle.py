from line import *



cv2.circle(image,(270,190),170, (255,0,0), 5)

cv2.imshow("Drawing of circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
