import cv2
import imutils
camera_id = 0
# Mở camera
capture = cv2.VideoCapture(camera_id)
rotate = 0
while True:
    # Đọc từng frame
    ret, frame = capture.read() 
    # Hiện ảnh
    if ret:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)
        cv2.imshow("Cam", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        rotate = 90
    elif key == ord('d'):
        rotate = -90
    elif key == ord('s'):
        rotate = 135
# Giải phòng camera
capture.release()
cv2.destroyAllWindows()