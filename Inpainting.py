# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:43:00 2020

@author: thejunaidiqbal
"""


import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath =  "images/abc.png"
    maskpath = "images/mask.jpg"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    mask= cv2.imread(maskpath, 0)
    
    output1 = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)
    
    output2 = cv2.inpaint(img, mask, 5, cv2.INPAINT_NS)

    output = [img, mask, output1, output2]
    titles = ['Damaged Image', 'Mask', 'TELEA', 'NS']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        if i == 1:
            plt.imshow(output[i], cmap='gray')
        else:
            plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


main()