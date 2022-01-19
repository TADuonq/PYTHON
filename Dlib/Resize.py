import cv2
import numpy as np

# read image
img = cv2.imread(r'C:\Users\Administrator\Duong\Python\Xulyanh\gaixinh.jpg')
print(img, img.shape)
img_pad = np.zeros([1000,1000,3])
img_pad += 100
img_pad[140:860] = img

cv2.imwrite(r'C:\Users\Administrator\Duong\Python\Xulyanh\gaixinh.jpg', img_pad)
print(r'C:\Users\Administrator\Duong\Python\Xulyanh\gaixinh.jpg', img_pad.shape)

print('Done')