#Nhập n số nguyên và k(0<k<=n, n>=5). Tổng k số hạng liên tiếp có tổng lớn nhất

# Thuật toán 1
n = -1
while(n < 5):
    n = int(input("Nhập n = "))

list = []
for i in range(n):
    x = int(input())
    list.append(x)
k = -1
while not(0 < k <= n):
    k = int(input("Nhập k = "))

s = 0
for i in range(k):
    s += list[i]
kq = s
for i in range(1, n - k + 1):
    s = 0
    for j in range(k):
        s = s + list[i + j]
    if kq < s:
        kq = s

print("Tổng k số hàng lớn nhất: ", kq)

# Thuật toán 2
n = -1
while(n < 5):
    n = int(input("Nhập n = "))

list = []
for i in range(n):
    x = int(input())
    list.append(x)
k = -1
while not(0 < k <= n):
    k = int(input("Nhập k ="))
s = 0
for i in range(k):
    s += list[i]
kq = s
for j in range(n - k):
    s = s + list[i + k] - list[i]
    if s > kq:
        kq = s
print("Tổng k số hàng lớn nhất: ", kq)