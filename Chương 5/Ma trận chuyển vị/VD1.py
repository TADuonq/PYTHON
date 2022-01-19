# Nhập ma trận A gồm m hàng và n cột. Tìm ma trận chuyển vị của A

m = -1
while m < 0 or m > 5:
    m = int(input("Nhập hàng m = "))
n = -1
while n < 0 or n > 5:
    n = int(input("Nhập số cột n = "))
A = [[int(input()) for j in range(n)] for i in range(n)]
print("Ma trận vừa nhập: ")
for i in range(m):
    for j in range(n):
        print(A[i][j], end = " ")
    print()

AT = [[A[i][j] for j in range(m)] for i in range(n)]
print("Ma trận chuyện vị: ")
for i in range(n):
    for j in range(m):
        print(AT[i][j], end = " ")
    print()