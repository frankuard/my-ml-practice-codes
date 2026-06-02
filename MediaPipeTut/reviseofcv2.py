import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import cv2

import time
prev = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Could not read the frame.")
        break
    frame = cv2.flip(frame,1)
    
    now = time.time()
    
    fps = int(1/(now -prev + 1e-9))
    prev = now
    cv2.putText(frame, f'FPS:{fps}',(20,40), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)
    
    
    cv2.imshow("Face Mesh Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting")
        break
cap.release()
cv2.destroyAllWindows()
