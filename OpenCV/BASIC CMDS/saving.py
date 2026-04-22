from displaying import *

if image is not None:
    output = cv2.imwrite("Pictures\Output_pic.png", image)
    print("Image Saved!")
else:
    print("Could not save the image!")