#Nhập só nguyên dương n. Tạo 1 danh sách gồm n số Fibonacci
#Xuất danh sách theo hàng, mỗi phần tử cách nhau 1 dấu cách " "

def Fibonacci():
    n = -1
    while (n < 0):
        n = int(input("Nhập n = "))
    A = [0 for i in range(n)]
    A[0] = 0
    A[1] = 1
    for i in range(2, n):
        A[i] = A[i - 1] + A[i - 2]
    return A, n

def Xuat(A, n):
    print("In dãy %d số Fibonacci: " % n, end="")
    for i in range(n):
        print(" ", A[i], end="")
A, n = Fibonacci()
Xuat(A, n)
