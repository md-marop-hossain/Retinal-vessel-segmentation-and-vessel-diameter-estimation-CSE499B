 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import math 
import diameter_calc  
 
 
img = cv2.imread("C:\\Users\\User\\retinalBloodVesselDiameterProject\\Images\\image.png") 
print("SIZE IS : {}".format(img.shape))
diameter_calc.diameter(img) 