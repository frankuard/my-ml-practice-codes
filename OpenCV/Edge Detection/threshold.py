import cv2

image = cv2.imread("Pictures/flower-729510_1280.jpg", cv2.IMREAD_GRAYSCALE)


ret, thres_img = cv2.threshold(image,120,255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Thresholded Image", thres_img)

cv2.waitKey(0)
cv2.destroyAllWindows()