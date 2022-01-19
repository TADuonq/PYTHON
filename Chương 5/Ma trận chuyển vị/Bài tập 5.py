#Nhập só nguyên dương n. Tạo 1 danh sách gồm n số Fibonacci nhỏ hơn n
#Xuất danh sách theo hàng, mỗi phần tử cách nhau 1 dấu cách " "

def Tao_Fibonacci():
    n = -1      #Thiết kế điều kiện lặp
    while(n < 0):
        n = int(input("Nhập n = "))
    A = []      #Khởi tạo list
    A.append(0)
    A.append(1)
    i = 1
    while A[i] + A[i - 1] < n:
        A.append(A[i] + A[i - 1])
        i = i + 1
    return A, n

def In_Fibonacci(A, n):
    print("In dãy số Fibonacci nhỏ hơn %d: " %n, end = "")
    for x in A:
        print(" ", x, end = "")

A, n = Tao_Fibonacci()
In_Fibonacci(A, n)