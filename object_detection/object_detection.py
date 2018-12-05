import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("dog1.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow('image_dog', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()