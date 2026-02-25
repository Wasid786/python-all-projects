import numpy as np
import cv2 

def get_limits(color: list[int]):
    c = np.array([[color]], dtype=np.uint8)
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    h = hsvC[0][0][0]

    lowerLimit = np.array([max(h - 10, 0), 100, 100], dtype=np.uint8)
    upperLimit = np.array([min(h + 10, 179), 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit