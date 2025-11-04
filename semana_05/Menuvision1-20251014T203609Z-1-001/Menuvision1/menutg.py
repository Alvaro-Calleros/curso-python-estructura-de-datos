import cv2 #Activar la libreria OpenCV en la variable cv2
import matplotlib.pyplot as plt #Activar la libreria de ploteo en la variable plt
import numpy as np     #Activar la libreria de manejo de matrices  en la variable np
import libtg
a=[73,4,3,2,63]
op=1
#alto = int(input("Teclea el alto de la figura :"))
#ancho= int(input("Tecela el ancho de la figura: "))
foto = 255*np.ones((400,500,3),dtype='uint8')

while(op!=9):
	print("Menu Funciones de Tranformaciones Geometricas ")
	print("1.-Tomar foto  2.-Traslacion  3.-Rotacion 4.-Cambio de tamaño 5.-Recorte 6.-Escala de grises 7.-Efecto marquesina 8.-Efecto Giro 9.-Salir")
	op=int(input("Seleccione una funcion: "))
	if(op==1):
		foto=libtg.tomafoto()
		plt.title("Para recortar ")
		plt.imshow(foto[:,:,::-1])
		plt.show()
	elif(op==7):
		libtg.marquecina(foto)
	else:
		print("No valido")