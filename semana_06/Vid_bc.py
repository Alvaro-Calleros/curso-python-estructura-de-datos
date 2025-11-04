
import numpy as np
import cv2
import Lvideo_alvaro as lva

aux = 0
aux_azul = 0
aux_rojo = 0
cap = cv2.VideoCapture(0)
color=(0, 255, 0)

pizarra1 = np.zeros((255,255,3), dtype=np.uint8)

cv2.line(pizarra1, (1,1), (1,255), (0,255,0), 3)
cv2.line(pizarra1, (252,1), (252,255), (0,255,0), 3)
cuenta_verde=0
cuenta_azul=0
cuenta_rojo=0

TH_ON = 21000
TH_OFF = 20000

while(cap.isOpened()):
    pizarra=pizarra1.copy()
    
    cv2.line(pizarra1, (1,1), (1,255), (0,255,0), 3)
    cv2.line(pizarra1, (252,1), (252,255), (0,255,0), 3)
    cv2.putText(pizarra1, 'Hola Upsin', (50,55), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(pizarra1, 'Arturo Y Alvaro', (50,200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

    verde_ini = np.array([38,31,23])
    verde_fin = np.array([97,255,255])
    
    azul_ini = np.array([110,50,50])
    azul_fin = np.array([130,255,255])
    
    blanco_ini = np.array([0, 0, 200])
    blanco_fin = np.array([180, 40, 255])


    rojo_ini1 = np.array([0, 70, 50])
    rojo_fin1 = np.array([10, 255, 255])
    rojo_ini2 = np.array([170, 70, 50])
    rojo_fin2 = np.array([180, 255, 255])

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, verde_ini, verde_fin)
    
    mask_azul = cv2.inRange(hsv, azul_ini, azul_fin)
    mask_rojo = cv2.inRange(hsv, rojo_ini1, rojo_fin1) | cv2.inRange(hsv, rojo_ini2, rojo_fin2)

    roi = mask[1 :480, 250:400]
    roi_azul = mask_azul[1 :480, 250:400]
    roi_rojo = mask_rojo[1 :480, 250:400]
    
    
    verdele=cv2.countNonZero(roi)
    azulele=cv2.countNonZero(roi_azul)
    rojole=cv2.countNonZero(roi_rojo)

    print(f"verde:{verdele} cuenta_verde:{cuenta_verde} | azul:{azulele} cuenta_azul:{cuenta_azul} | rojo:{rojole} cuenta_rojo:{cuenta_rojo}")

    if verdele < TH_OFF and aux==1:
        aux=0
    elif verdele > TH_ON and aux==0:
        aux=1
        cuenta_verde += 1

    if azulele < TH_OFF and aux_azul==1:
        aux_azul=0
    elif azulele > TH_ON and aux_azul==0:
        aux_azul=1
        cuenta_azul += 1

    if rojole < TH_OFF and aux_rojo==1:
        aux_rojo=0
    elif rojole > TH_ON and aux_rojo==0:
        aux_rojo=1
        cuenta_rojo += 1

    cv2.putText(pizarra, f'verdes: {cuenta_verde}', (50,70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
    cv2.putText(pizarra, f'azules: {cuenta_azul}', (50,85), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
    cv2.putText(pizarra, f'rojos: {cuenta_rojo}', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

    cv2.imshow('Pizarra', pizarra)
    cv2.imshow('Area verde', roi)
    cv2.imshow('Area Azul', roi_azul)
    cv2.imshow('Area Rojo', roi_rojo)
    key = cv2.waitKey(1) & 0xFF
        
    if key == ord('q'):  
        break
    elif key == ord('r'):  
        mask = cv2.inRange(hsv, azul_ini, azul_fin)


cap.release()
cv2.destroyAllWindows()