import numpy as np
import cv2
import Lvideo_alvaro as lva

cap = cv2.VideoCapture(0)

color_actual = [0, 0, 255]  

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if not ret:
        break

    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    ret, frame_bin = cv2.threshold(frame_gris, 127, 255, cv2.THRESH_BINARY)
    ret, frame_bin_inv = cv2.threshold(frame_gris, 127, 255, cv2.THRESH_BINARY_INV)
    
    cnt, hier = cv2.findContours(frame_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(frame, cnt, -1, (0, 255, 0), 2)
   
    frame_contorns = frame.copy()
    cv2.drawContours(frame_contorns, cnt, -1, (0, 255, 0), 2)
    
    # Usar el color actual
    acolor = lva.cambia_color_numpy(color_actual, frame_bin)

    cv2.imshow('Ventana3', acolor)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):  
        break
    elif key == ord('r'):  
        color_actual = [0, 0, 255]  

    elif key == ord('g'):  
        color_actual = [0, 255, 0]  

    elif key == ord('b'):  
        color_actual = [255, 0, 0]  


cap.release()
cv2.destroyAllWindows()