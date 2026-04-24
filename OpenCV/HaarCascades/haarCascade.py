import cv2

face_cascade = cv2.CascadeClassifier("Haar Cascades XML Files\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    detect_face = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    """
    detect multi scale is - scan and detect faces
    1.1 balance not too slow, blind
    
    minneightbours =  5
    """
    
    for (x,y,w,h) in detect_face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        """
        for loop going through each face
        face = [100,150,180,230]
        maybe its a face 1?
        another similar data face 2 [120,450,670 or smth]
        
        x = how far from left
        y = how far from top
        w = width of face
        h = height of face
        
        """
        
    cv2.imshow("Webcam Face Detection", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

        