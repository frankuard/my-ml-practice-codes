from resize import *

# if image is not None:
    
#     (h,w) = image.shape[:2]
    
#     center = (w//2, h//2)
    
#     R = cv2.getRotationMatrix2D(center, 90, 1.0)
    
#     rotated = cv2.warpAffine(image, R, (w,h))
    
#     cv2.imshow("Original Image", image)
#     cv2.imshow("Rotated Image", rotated)
    
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()