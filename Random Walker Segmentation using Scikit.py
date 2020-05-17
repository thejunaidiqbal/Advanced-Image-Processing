# -*- coding: utf-8 -*-
"""
Created on Sun May 17 03:03:34 2020

@author: thejunaidiqbal
"""

import matplotlib.pyplot as plt
from skimage import io, img_as_float
import numpy as np


img = img_as_float(io.imread("images/Alloy_noisy.jpg"))

#plt.hist(img.flat, bins=100, range=(0, 1)) 


from skimage.restoration import denoise_nl_means, estimate_sigma

sigma_est = np.mean(estimate_sigma(img, multichannel=True))
denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True, 
                               patch_size=5, patch_distance=3, multichannel=True)
                           
#plt.hist(denoise_img.flat, bins=100, range=(0, 1)) 

from skimage import exposure

#eq_img = exposure.equalize_hist(denoise_img)
eq_img = exposure.equalize_adapthist(denoise_img)
#plt.imshow(eq_img, cmap='gray')
#plt.hist(denoise_img.flat, bins=100, range=(0., 1))


markers = np.zeros(img.shape, dtype=np.uint)

markers[(eq_img < 0.8) & (eq_img > 0.7)] = 1
markers[(eq_img > 0.85) & (eq_img < 0.99)] = 2

from skimage.segmentation import random_walker

labels = random_walker(eq_img, markers, beta=10, mode='bf')
plt.imsave("images/markers.jpg", markers)
segm1 = (labels == 1)
segm2 = (labels == 2)
all_segments = np.zeros((eq_img.shape[0], eq_img.shape[1], 3))

all_segments[segm1] = (1,0,0)
all_segments[segm2] = (0,1,0)

#plt.imshow(all_segments)

from scipy import ndimage as nd

segm1_closed = nd.binary_closing(segm1, np.ones((3,3)))
segm2_closed = nd.binary_closing(segm2, np.ones((3,3)))

all_segments_cleaned = np.zeros((eq_img.shape[0], eq_img.shape[1], 3)) 

all_segments_cleaned[segm1_closed] = (1,0,0)
all_segments_cleaned[segm2_closed] = (0,1,0)

plt.imshow(all_segments_cleaned) 
plt.imsave("images/rw.jpg", all_segments_cleaned)







