import cv2

image = cv2.imread("Part 1\student id card.png")

if image is None:
    print("Error the image is not found!!")

else:
    print("Image loaded succesfully")