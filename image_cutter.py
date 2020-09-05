import cv2
import numpy as np

cap = cv2.VideoCapture(0)
t0 = cap.read()[1]
t1 = cap.read()[1]

grey1 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)

grey2 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)

blur1 = cv2.GaussianBlur(grey1,(7,7),0)

blur2 = cv2.GaussianBlur(grey2,(5,5),0)

d = cv2.absdiff(blur1, blur2)

ret, th = cv2.threshold( d, 10, 255, cv2.THRESH_BINARY )
dilated=cv2.dilate(th, None, iterations=1)

contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(c) for c in contours]