# Cho số nguyên dương n (0 < n <= 10**12). Kiểm tra xem n có phải là số nguyên tố hay không

# Cách 1
from asyncio.format_helpers import _format_callback_source


n = int(input("Nhap so tu nhien n = "))
while n < 0 or n > 10**12:
    n = int(input("Nhap so tu nhien n = "))
ok = 1
if n < 2:
    ok = 0
else:
    for i in range(2, n - 1):
        if n % i == 0:
            ok = 0
            break
if ok == 1:
    print(n, "la so nguyen to.")
else:
    print(n, "khong la so nguyen to.")

#Cách 2
n = int(input("Nhap so tu nhien n = "))
while n < 0 or n > 10**12:
    n = int(input("Nhap so tu nhien n = "))
if n < 2:
    print(n, "khong la so nguyen to.")
else:
    a = 2
    nt = True
    while a*a <= n:
        if n % a == 0:
            nt = False
            break
        a += 1
    if nt:
        print(n, "la so nguyen to.")
    else:
        print(n, "khong la so nguyen to.")