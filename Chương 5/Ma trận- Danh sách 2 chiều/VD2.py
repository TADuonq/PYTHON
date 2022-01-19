# Ciết chương trình nhập vào 1 ma trận gồm m hàng và n cột (0 <= m, n<=5)
# In ra ma trận được nhập

m = -1
while m < 0 or m > 5:
    m = int(input("Nhập hàng m = "))
n = -1
while n < 0 or n > 5:
    n = int(input("Nhập số cột n = "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    A.append(row)
for x in A:
    print(x)