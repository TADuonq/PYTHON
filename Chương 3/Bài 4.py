# Tính tổng các chữ số

from turtle import st


st = input("Nhập chuỗi: ")
s = 0
for x in st:
    if x.isdigit():
        s = s + int(x)
print("Tổng các chữ số trong chuỗi s: ", s)