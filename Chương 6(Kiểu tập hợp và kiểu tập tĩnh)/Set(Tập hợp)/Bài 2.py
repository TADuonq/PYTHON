# Taoh 1 danh sách gồm n số nguyên ngẫu nhiên trong khoảng [1,10]
# Liệt kê số lần xuất hiện của các số trong danh sách?

from random import * 
n = int(input("Nhập n = "))
A = [randint(0,10) for i in range(n)]
print("Dãy %d số ngẫu nhiên trong khoảng [0,10]: " %n)
print(A)
setA = set(A)
for x in setA:
    print("Số %2d"%x, "xuất hiện: ", A.count(x))