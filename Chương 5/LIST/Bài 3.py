# Sàng số nguyên tố Eratosthenes



N = -1
while N <= 0:
    N = int(input("Nhập N = "))
list = []
for i in range(N + 1):
    list.append(1)
list[0] = list[1] = 0
can2 = int(N**(1/2))
for i in range(2, 1 + can2):
    if list[i] == 1:
        k = i
        while i * k <= N:
            list[i*k] = 0
            k = k + 1
print("Danh sách các số nguyên tố trong khoảng từ 1 đến N: ")
for i in range(N + 1):
    if list[i] == 1:
        print(i, end = " ")