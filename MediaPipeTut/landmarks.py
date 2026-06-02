## IMPORTING REQUIRED LIBRARIES AND MODELS

import cv2
import time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import HandLandmarker, HandLandmarkerOptions 
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode as VisionRunningMode


## CREATING DETECTOR - ONE TIME ONLYY

## IMPORTING  .TASK I.E THE TRAINED AI MODEL FOR HAND DETECTION 
base_options = python.BaseOptions(model_asset_path="models/hand_landmarker.task")

## HOW SHOULD IT BEHAVE IS U(NDER THIS 
latest_result = [None]

def on_result(result,output_image,timestamp_ms):
    latest_result[0] = result
    
    
options = HandLandmarkerOptions(base_options=base_options,running_mode=VisionRunningMode.LIVE_STREAM,num_hands=2,min_hand_detection_confidence = 0.5,result_callback=on_result)


## CREATING A TASK OBJECT

landmarker  = HandLandmarker.create_from_options(options)
print("HandLandMarker created successfully")


## FOR THE CAMERA PART

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    ## CONVERTING BGR TO RGB
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB,data= frame_rgb)
    
    timestamp_ms = int(time.time()* 1000)
    landmarker.detect_async(mp_image,timestamp_ms)
    
    
    ## WE ARE GRABBING THE NEWEST DETECTION HAND RESULT
    result = latest_result[0]
    
    ## PRINTING FOUND LANDMARK IF IT FINDS IT
    
    if result and result.hand_landmarks:
        print("Landmarks Found")
        
    
    cv2.imshow("Hand Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
landmarker.close()

