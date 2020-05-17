# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:46:42 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt

def main():
    
    impath = "images/abc.png"
    img = cv2.imread(impath, 0)
      
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(), 256, [0, 255])
    plt.title('Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()


main()