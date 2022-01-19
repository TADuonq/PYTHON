# Nhập ma trận A gồm m hàng và n cột. Tìm ma trận chuyển vị của A

def Nhap():
    m = int(input("Nhập hàng m = "))
    n = int(input("Nhập cột n = "))
    A = [[int(input("A[%d][%d] = "%(i,j))) for j in range(n)] for i in range(m)]
    return A

def Xuat(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end = " ")
        print()

def Chuyenvi(A):
    C = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    return C

print("Nhập ma trận: ")
A = Nhap()
print("In ma trận: ")
Xuat(A) 
AT = Chuyenvi(A)
Xuat(AT)