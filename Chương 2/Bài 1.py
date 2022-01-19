# Cho số tự nhiên n(0 <= n <=10**1000). Tính tổng các chữ số của n

n = int(input("Nhap so tu nhien n = "))
while n < 0 or n > 10**1000:
    n = int(input("Nhap so tu nhien n = "))
tong = 0
while n > 0:
    tong = tong + n % 10
    n = n // 10
print("Tong cac chu so cua n: ", tong)