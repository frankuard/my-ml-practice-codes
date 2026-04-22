import cv2

img = cv2.imread("Pictures/col boi.jpg")

if img is not None: 
    print("Image loaded succesfully")
    
    cv2.imshow("Windows Title",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    output = cv2.imwrite("Pictures\Output_colboi.png",img)
    
    h,w,c = img.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray one", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image didnt load succesfully")