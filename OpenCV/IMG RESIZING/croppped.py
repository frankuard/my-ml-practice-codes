from resize import *

if image is not None:
    cropped = image[400:900, 400:800]
    
    cv2.imshow("Original Image",image)
    cv2.imshow("Cropped Image",cropped)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    