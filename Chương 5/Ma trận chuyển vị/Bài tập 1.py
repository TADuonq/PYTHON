#Nhâm 2 ma trận cấp m x k và k x n

#Cách 1
m = int(input("Nhập m = "))
k = int(input("Nhập k = "))
n = int(input("Nhập n = "))
print("Nhập ma trận A: ")
A = [[int(input())for j in range(n)] for i in range(m)]
print("Nhập ma trận B: ")
B = [[int(input())for j in range(n)] for i in range(k)] 

C = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        for t in range(k):
            C[i][j] += A[i][j] * B[i][j]

print("In ra ma trận tích C = A.B ")
for i in range(m):
    for j in range(n):
        print(C[i][j], end = " ")
    print()

#Cách 2
def Nhap():
    m = int(input("Nhập hàng: "))
    n = int(input("Nhập cột: "))
    A = [[int(input())for j in range(n)] for i in range(m)]
    return A, m, n

def Xuat(A, m, n):
    for i in range(m):
        for j in range(n):
            print(A[i][j], end = " ")
        print()

def NhanMT(A, B, m, n):
    C = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            for t in range(k):
                C[i][j] = A[i][t] * B[j][t]

    return C