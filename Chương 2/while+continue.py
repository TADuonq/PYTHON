# Tính tổng các số Fibonacci chi hết cho 3 nhỏ hơn N
from re import A


n = int(input("Nhập số dương N: "))
tong, a, b = 0, 0, 1
while b < n:
    a, b = b, a + b
    if 0 != a % 3:          # Bỏ qua nếu không chia hết cho 3
        continue
    tong += a
print('Tổng là: ', tong)