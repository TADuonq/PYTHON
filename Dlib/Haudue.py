import cv2
import dlib
import numpy as np

img = cv2.imread(r'C:/Users/Administrator/Duong/Python/Dlib/haudue.jpg')


gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)

face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r'C:\Users\Administrator\Duong\Python\Dlib\shape_predictor_68_face_landmarks.dat')
faces = face_detector(gray)
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(img = img, pt1 = (x1,y1), pt2 = (x2,y2), 
                  color = (0,255,0), thickness = 3)
    face_features = predictor(image = gray, box = face)
    for n in range(0,68):
        x = face_features.part(n).x
        y = face_features.part(n).y
        cv2.circle(img = img, center = (x,y), radius = 2, color = (0,0,255), thickness = 1)
cv2.imshow(winname = "Face Recognition App", mat = img)

cv2.waitKey()
cv2.destroyAllWindows()