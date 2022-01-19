# Nhập số nguyên dương n(n>5)
# Nhập dãy số n số nguyên
#Xuất dãy số theo hàng, mỗi phần tử cách nhau 1 dấu ","
#Tìm min, max

def Nhap():
    n = -1
    while(n <= 5):
        n = int(input("Nhập n = "))
    print("Nhập các phần tử của dãy số: ")
    A = [int(input())for i in range(n)]
    return A,n

def Xuat(A, n):
    print("In lại dãy số: ", end = " ")
    for i in range(n):
        if i != n - 1:
            print(A[i], end = ",")
        else:
            print(A[i])

def Nguyen_to(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def In_nguyen_to(A,n):
    print("In số nguyên tố: ", end = " ")
    for i in range(n):
        if Nguyen_to(A[i]):
            print(" ", A[i], end = " ")

A,n = Nhap()
Xuat(A,n)
In_nguyen_to(A,n)