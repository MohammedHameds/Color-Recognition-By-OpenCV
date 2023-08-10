import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    ret , frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height,width,_ = hsv_frame.shape
    
    center_x = int(width/2)
    center_y = int(height/2)
    
    pixel_center = hsv_frame[center_y, center_x] 
    hue_value = pixel_center[0]
        
    color = "Undefined"
    if hue_value < 5 :
        color = "Red"
    elif hue_value < 22 :
        color = "Orange"
    elif hue_value < 33 :
        color = "Yellow"
    elif hue_value < 78 :
        color = "Green"
    elif hue_value < 131 :
        color = "Blue"
    elif hue_value < 170 :
        color = "Violet"  
    else :    
        color = "Red"
    
    pixel_center_bgr = frame[center_y, center_x] 
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    
    cv2.rectangle(frame,(center_x-200,10),(center_x+200,120),(255,255,255),-1)
    cv2.putText(frame,color,(center_x-200,100),0,3,(b,g,r),5)
    cv2.circle(frame,[center_x,center_y],2,(0,0,0),2)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(27) == ord('q') :
        break
        
cap.release()    
cv2.destroyAllWindows()    