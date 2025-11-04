import matplotlib.pyplot as plt
import cv2
import Lvideo_alvaro as lva

image = cv2.imread("C:\\Users\\alvar\\Desktop\\DESK\\UNI\\4to CUATRIMESTRE\\Estructura de Datos\\python\\gris.jpg")

#print(image.shape)
frame_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, frame_bin = cv2.threshold(frame_gris,127,255,cv2.THRESH_BINARY)

acolor = lva.cambr_color_normal([255,0,0], frame_bin)

plt.imshow(acolor)
plt.show(block=False)
plt.pause(0.2)
# plt.waitforbuttonpress() # espera a que se presione una tecla pixel por pixel
# plt.close()
        
plt.waitforbuttonpress() # espera a que se presione una tecla para cerrar toda la imagen
plt.close()
    