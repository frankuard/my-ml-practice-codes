import cv2

image = cv2.imread("Pictures/lake.jpg")

blurred = cv2.medianBlur(image,11)

cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blurred)
  
cv2.waitKey(0)
cv2.destroyAllWindows()