from math import gcd
a = int(input("Nhap so nguyen duong a: "))
b = int(input("Nhap so nguyen duong b: "))
c = int(input("Nhap so nguyen duong c: "))
d = gcd(a,b)
gcd_max = gcd(d,c)
print("UCLN cua 3 so a, b, c: ", gcd_max)