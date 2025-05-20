import numpy as np

from skimage import io
photo = io.imread('bts.png')
print(type(photo))  #type is array

print(photo.shape) #(row,col, color=3 rgb)


#display image

import matplotlib.pyplot as plt
plt.imshow(photo)
#plt.axis('off') #remove axis
plt.show #show image

#to run image in vs code: Open the command palette (Ctrl + Shift + P) → Search 
# "Python: Run Current File in Interactive Window" → Select it.

#reverse upside down img
plt.imshow(photo[::-1])
#plt.axis('off') #remove axis
plt.show #show image

#mirror image. reverse col
plt.imshow(photo[:,::-1])
#plt.axis('off') #remove axis
plt.show #show image

#crop photo
plt.imshow(photo[50:150, 150:280])
#plt.axis('off') #remove axis
plt.show #show image

#half the size of row n col
plt.imshow(photo[::2, ::2])
#plt.axis('off') #remove axis
plt.show #show image

#change color hue base on rgb
photo_masked = np.where(photo > 100,255,0)
plt.imshow(photo_masked)
plt.show #show image

#transpose array - lanscape to potrait
plt.imshow(photo[:,:,0].T)
plt.show

#mathematical function
photo
photo_sin = np.sin(photo)
print(photo_sin)

print(np.sum(photo))
print(np.prod(photo))
print(np.mean(photo))
print(np.std(photo))
print(np.var(photo))
print(np.min(photo))
print(np.max(photo))
print(np.argmin(photo))
print(np.argmax(photo))





