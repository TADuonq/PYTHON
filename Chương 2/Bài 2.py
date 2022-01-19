# Cho số tự nhiên n(0 <= n <=10**1000). Tìm chữ số MAX và MIN trong n

n = int(input("Nhap so tu nhien n = "))
while n < 0 or n > 10**1000:
    n = int(input("Nhap so tu nhien n = "))
min_so = 9      #chu so nho nhat
max_so = 0      #chu so lon nhat
if n < 10:
    max_so = min_so = n
else:
    while n > 0:
        u = n % 10
        max_so = max(u, max_so)
        min_so = min(u, min_so)
        n = n // 10
print("Chu so lon nhat: ", max_so)
print("Chu so nho nhat: ", min_so)