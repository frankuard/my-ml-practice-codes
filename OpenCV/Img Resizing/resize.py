import cv2

image = cv2.imread("Pictures/col boi.jpg")

resized = cv2.resize(image,(500,500))

# cv2.imshow("Resized Image",resized)

# cv2.imshow("Original Image",image)


# cv2.imwrite("Pictures/Resized_Output.png",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
