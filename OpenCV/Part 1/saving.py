from displaying import *

if image is not None:
    output = cv2.imwrite("Part 1\Output_pic.png", image)
    print("Image Saved!")
else:
    print("Could not save the image!")