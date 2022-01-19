#Viết chương trình nhập vào 1 bộ(tuple) gồm n số nguyên
#Lưu các số chính phương có trong tuple P trong tuple CP

from math import *
n = -1
while(n < 0):
    n = int(input("Nhập n = "))
print("Nhập", n, "phần tử cho Tuple: ")
P = tuple(int(input()) for i in range(n))
print("Tuple vừa nhập, P = ", P)
CP = tuple(x for x in P if x**(0.5) == int(x**(0.5)))
print("Tuple số chính phương trong P: ", CP)


