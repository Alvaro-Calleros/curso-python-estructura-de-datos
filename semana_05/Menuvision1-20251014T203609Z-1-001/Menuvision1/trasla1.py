import numpy as np
import cv2


imagen = cv2.imread("d:/Upsin/2025/Grupos/4-3/temp/foto.jpg")
title="foto"
cv2.imshow(title,imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()


x=int(input("X="))
y=int(input("Y="))
movida = imagen
	 


 
ancho = imagen.shape[1]
alto = imagen.shape[0]
x=0
dire="derecha"
while(1):
	M = np.float32([[1,0,x],[0,1,y]])
	movida = cv2.warpAffine(imagen,M,(ancho,alto))
		
	cv2.imshow(title,movida)
	if(dire=="derecha"):
		x=x+1
	if(dire=="izquierda"):
		x=x-1
	
	if(x>=150):
		dire="izquierda"
	elif(x<=-150):
		dire="derecha"
		



	if (cv2.waitKey(1) & 0xFF == ord('q')):#si la tecla presionada es q salir
			break
	
	
