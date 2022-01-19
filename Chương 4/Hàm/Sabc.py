# Đọc toạ độ 3 điểm ABC và đưa ra diện tích tam giác ABC nếu thoả mãn

from math import *
def toado():
    x = float(input("Nhập hoành độ: "))
    y = float(input("Nhập tung độ:"))
    return x,y

def kc(Ax,Ay, Bx, By):
    return sqrt(pow(Ax-Bx, 2) + pow(Ay - By, 2))

Ax, Ay = toado()
Bx, By = toado()
Cx, Cy = toado()
a = kc(Ax, Ay, Bx, By)
b = kc(Bx, Ay, Bx, By)
c = kc(Cx, Cy, Ax, Ay)
p = (a + b + c) / 2
S = sqrt(p * (p-a) * (p-b) * (p-c))
print("Diện tích tam giac ABC là S = %f" %S)