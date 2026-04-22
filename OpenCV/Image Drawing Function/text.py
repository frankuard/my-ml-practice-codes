from circle import *




cv2.putText(image, "Hello Python Programmers", (140,300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)

cv2.imshow("Text Having Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()