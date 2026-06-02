## IMPORTING REQUIRED LIBRARIES AND MODELS

import cv2
import time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.vision import HandLandmarker
from mediapipe.tasks.python.vision.core.vision_task_running_mode import VisionTaskRunningMode as VisionRunningMode


## CREATING DETECTOR - ONE TIME ONLYY

## IMPORTING  .TASK I.E THE TRAINED AI MODEL FOR HAND DETECTION 
base_options = python.BaseOptions(model_asset_path="models/hand_landmarker.task")

## HOW SHOULD IT BEHAVE IS U(NDER THIS 

def on_result(result,output_image,timestamp_ms):
    pass

options = HandLandmarker.HandLandmarkerOptions(base_options=base_options,running_mode=VisionRunningMode.LIVE_STREAM,num_hands=2,min_hand_detection_confidence = 0.5,result_callback=on_result)


## CREATING A TASK OBJECT

landmarker  = HandLandmarker.create_from_options(options)
print("HandLandMarker created successfully")
landmarker.close()


