
# coding: utf-8

# In[9]:

from Tkinter import *
import cv2
import Tkinter, tkFileDialog
import numpy as np
from ITC_Support import *
from ITC_main import *

root = Tkinter.Tk()
root.withdraw()

path = tkFileDialog.askopenfilename()
encoded,original = encode(path)

cv2.namedWindow('Compressed Image', cv2.WINDOW_NORMAL)
cv2.imshow('Compressed Image',encoded)

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image',original)

cv2.waitKey(0)
cv2.destroyAllWindows()

