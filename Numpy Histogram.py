# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:48:32 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    impath = "images/abc.png"
    img = cv2.imread(impath, 0)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    hist, bins = np.histogram(img.ravel(), 256, [0,255])
    plt.xlim([0, 255])
    plt.ylim([0, 3000])
    plt.plot(hist)
    plt.title('Histogram')
    plt.show()


main()