# Tổng chéo chính, chéo phụ của ma trận n hàng n cột
# Phần tử lớn nhất, nhỏ nhất của ma trận

n = int(input("Nhập n = "))
print("Nhập ma trận: ")
A = [[int(input("A[%d][%d] = "%(i,j))) for j in range(n)] for i in range(n)]
print("In lại ma trận: ")
for i in range(n):
    for j in range(n):
        print(A[i][j], end = " ")
    print()
chinh = phu = 0
for i in range(n):
    chinh += A[i][i]
    phu += A[i][n - 1 - i]
print("Tổng đường chéo chính: ", chinh)
print("Tổng đường chéo phụ: ", phu)
minA = maxA = A[0][0]
for i in range(n):
    for j in range(n):
        if maxA < A[i][j]:
            maxA = A[i][j]
        if minA > A[i][j]:
            minA = A[i][j]
print("Phần tử lớn nhất: ",maxA)
print("Phần tử nhỏ nhất: ",minA)