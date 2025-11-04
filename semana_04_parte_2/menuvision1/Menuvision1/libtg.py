import cv2 #Activar la libreria OpenCV en la variable cv2
import matplotlib.pyplot as plt #Activar la libreria de ploteo en la variable plt
import numpy as np     #Activar la libreria de manejo de matrices  en la variable np
def tomafoto():
	cap = cv2.VideoCapture(0)
	leido,frame = cap.read()
	print(leido)
	if leido == True:
		print("Foto tomada correctamente")
	else:
		print("Error al acceder a la cámara")
		cap.release()
	return frame
def marquecina(img):
	x=0
	inc=1
	while(1):
		# #Traslacion
		M = np.float32([[1,0,x],
 	            		[0,1,0]])
		traslacion = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
		x=x+inc
		if(x>=500):
			inc=-1
		if(x<0):
			inc=1
		cv2.imshow("Rebote",traslacion)
		if (cv2.waitKey(1) & 0xFF == ord('q')):#si la tecla presionada es q salir
			break