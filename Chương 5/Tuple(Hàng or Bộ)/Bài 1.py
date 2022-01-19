# Tạo 1 danh sách n số nguyên bằng cách tạo ngẫu nhiên trong khoảng [0,10]
# Hãy thống kê danh sách xem mỗi phần tử xuất hiên bao nhiêu lần

from random import *
n = int(input("Nhập n = "))
print("Tạo dãy n số ngẫu nhiên trong khoảng [0,10]")
A = [randint(0,10) for i in range(n)]
for i in range(n):
    if i != n - 1:
        print(A[i], end = " ")
    else:
        print(A[i])
setA = set (A)
for x in setA:
    print(x, "xuất hiện: ", A.count(x))
    