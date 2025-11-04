import cv2

image = cv2.imread("C:\\Users\\alvar\\Desktop\\DESK\\UNI\\4to CUATRIMESTRE\\Estructura de Datos\\python\\gris.jpg")

print(image.shape)

cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Imagen", 803, 682) # imagen proporcionalmente alargada para evitar que se distorsione o se vea pixelada

for i in range(0,13,1):
    for j in range(0,11,1):
        print(i," ", j, " ", image[i][j])
        image[i][j][1] = 255
        image[i][j][0] = 0
        image[i][j][2] = 0
        cv2.imshow("Imagen", image)
        cv2.waitKey(100)
        # plt.waitforbuttonpress() # espera a que se presione una tecla pixel por pixel
        # plt.close()

cv2.waitKey(0) # espera a que se presione una tecla para cerrar toda la imagen
cv2.destroyAllWindows()
    