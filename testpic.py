import cv2             #Dies ist die Bildverarbeitungsbibliothek OpenCV
import numpy as np     #Rechnen mit vielen Zahlen in einem Array (z. B. Bilder)

fn = 'testpic001.png'
img = cv2.imread(fn) 

print("Dimensionen von img: (Höhe, Breite, Farbkanäle)", img.shape)
