import cv2
import random

img = cv2.imread('assets/test.jpg', -1)
#print(img) #numpy array
#print(img.shape)  #height, width and channels(color values, bgr)
'''
accessing image pixels as rows and columns of an array
'''
#print(img[0])
#print(img[257][45:400])
#print(img[257][40])

'''
changing color values for pixels in the first 100 rows of the img
'''
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randrange(255), random.randrange(255), random.randrange(255)]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('assets/random.jpg', img)

'''
copying and pasting a section of the image
'''

tag = img[275:400, 320:450]
img[375:500, 400:530] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
