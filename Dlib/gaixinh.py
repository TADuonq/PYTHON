import cv2
import imutils


# Đọc ảnh
img = cv2.imread(r'C:/Users/Administrator/Duong/Python/Dlib/gaixinh.jpg')

# Show ảnh
cv2.imshow("Gai xinh", img) 

# Lưu ảnh
'''cv2.imwrite("gaixinh_gray.jpg", img)'''

# Dùng màn hinh 
cv2.waitKey()
 

# Đổi màu ảnh
'''img_gray = cv2.cvtColor(img,  cv2.COLOR_BGR2HSV_FULL)
cv2.imshow("Gai xinh", img_gray) 
cv2.waitKey()'''

# Thay đổi khung ảnh
'''img_rs = cv2.resize(img, dsize = None, fx = 2, fy = 2, interpolation = False)
cv2.imshow("Gai xinh", img_rs) 
cv2.waitKey()'''

# Quay ảnh hàm imutils 
img_rotate = imutils.rotate(img, 90)
cv2.imshow("Gai xinh", img_rotate) 
cv2.waitKey()

# Convert thành ảnh xám
#gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# AP threshold
'''ret, cv2.THRESH_BINARY = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Gai xinh", gray_img) 
cv2.waitKey()

edges = cv2.Canny(gray_img, threshold1 = 100, threshold2 = 200)
cv2.imshow("Gai xinh", edges) 
cv2.waitKey()'''

# Làm mờ, giảm nhiễu
'''blur = cv2.GaussianBlur(img, ksize = (31,31), sigmaX = 0)
cv2.imshow("Gai xinh", blur) 
cv2.waitKey()'''

# Đóng các cửa sổ
cv2.destroyAllWindows()