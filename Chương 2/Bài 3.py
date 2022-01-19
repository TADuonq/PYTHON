# Cho 2 số nguyên dương a và b (0 < a,b <= 10**9). Tìm UCLN và BCNN

# Cách 1
a = int(input("Nhap so nguyen duong a = "))
while a <= 0 or a > 10**9:
    a = int(input("Nhap so nguyen duong a = "))
b = int(input("Nhap so nguyen duong b = "))
while b <= 0 or b > 10**9:
    b = int(input("Nhap so nguyen duong b = "))
x = a
y = b
#Tìm UCLN theo thuật thoán Eculid
while b > 0:
    r = a % b
    a = b 
    b = r
ucln = a
bcnn = x*y//ucln
print("UCLN cua a va b: ", ucln)
print("BCNN cua a va b: ", bcnn)

#Cách 2
a = int(input("Nhap so nguyen duong a = "))
while a <= 0 or a > 10**9:
    a = int(input("Nhap so nguyen duong a = "))
b = int(input("Nhap so nguyen duong b = "))
while b <= 0 or b > 10**9:
    b = int(input("Nhap so nguyen duong b = "))

from math import gcd
print("UCLN cua a va b: ", gcd(a,b))
print("BCNN cua a va b: ", a*b//gcd(a,b))