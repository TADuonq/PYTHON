# Dãy con tăng dài nhất: xét dãy số a gồm n số nguyên

n = int(input("Nhập n = "))
print("Nhập", n, "phần tử: ")
a = [int(input())for i in range(n)]
L = [1 for i in range(n)]
i = n - 2
while i > 0:
    for t in range(i + 1, n):
        if a[i] < a[t]:
            L[i] = max(L[i], 1 + L[i])
    i -= 1
print("Độ dài của dãy con tăng dài nhất: ", max(L))
