import numpy as np
import cv2

bgr = np.zeros((300,300,3), dtype=np.uint8)
bgr = np.ones((300,300,3), dtype=np.uint8)

# bgr[:,:,0] = 255 # para azul
# bgr[:,:,1] = 255 # para verde
# bgr[:,:,2] = 255 # para rojo

# bgr[:,:] = 75 # para blanco y negro


print(bgr.shape)
print(type(bgr))

cv2.imshow('Ventana', bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()



