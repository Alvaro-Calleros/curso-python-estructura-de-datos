import numpy as np

import cv2

def cambr_color_normal(color, img_bin):
    filas = img_bin.shape[0]
    columnas = img_bin.shape[1]
    
    img_color = np.zeros((filas, columnas, 3), dtype=np.uint8)
    
    for i in range(filas):
        for j in range(columnas):
            if img_bin[i][j] == 255:
                img_color[i][j] = color
    return 

def cambia_color_numpy (color, mascara):
    filas = mascara.shape[0]
    columnas = mascara.shape[1]
    img_color = np.zeros((filas, columnas, 3), dtype=np.uint8)
    
    img_color[mascara == 255] = color
    return img_color