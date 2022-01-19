# Biết rằng: Số tự nhiên n được gọi là số hoàn hảo nếu tổng các ước số của n bằng đúng 2n.
# Ví dụ: n = 6 có các ước là 1, 2, 3, 6 và có 1 + 2 + 3 + 6 = 12
# Viết chương trình nhâp vào STN n(0 <= n <= 10**12)

# Kiểm tra số hoàn hảo
from re import I


n = int(input("Nhap so tu nhien n = "))
while n < 0 or n > 10**12:
    n = int(input("Nhap so tu nhien n = "))
# Chỉ xét n là số nguyên dương
s = 0
for i in range(1, n + 1):
    if n % i == 0:
        s = s + i
if n > 0 and s == 2*n:
    print(n, "la so hoan hao!")
else:
    print(n, "khong la so hoan hao!")