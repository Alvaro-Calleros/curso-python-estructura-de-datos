import cv2
import numpy as np

img = cv2.imread("C:\\Users\\alvar\\Desktop\\DESK\\UNI\\4to CUATRIMESTRE\\Estructura de Datos\\python\\foto.jpg")


cv2.imshow("Su foto 8-3 ",img)

cv2.waitKey(0)
cv2.destroyAllWindows()



ancho=img.shape[1]
alto = img.shape[0]
puntoRotacion = (ancho//2, alto//2)
R = ancho/alto
x=1
giro=1

grados=0
dire="derecha"

while(1):
	M = cv2.getRotationMatrix2D(puntoRotacion,grados, 1.0)
	imagenRotada = cv2.warpAffine(img, M, (ancho, alto))

	cv2.imshow("Imagen rotada",imagenRotada)
	if(dire=="derecha"):
			grados=grados +1
	if(dire=="izquierda"):
			grados=grados -1

	if (cv2.waitKey(1) & 0xFF == ord('q')):
		break
	if (cv2.waitKey(1) & 0xFF == ord('d')):
		dire="derecha"
	if (cv2.waitKey(1) & 0xFF == ord('i')):
		dire="izquierda"

###########

#newAncho = x
#newAlto = int(newAncho/R)
#img = cv2.resize(img, (newAncho, newAlto), interpolation=cv2.INTER_AREA)