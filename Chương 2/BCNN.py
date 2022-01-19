from math import gcd
a = int(input("Nhap so nguyen duong a: "))
b = int(input("Nhap so nguyen duong b: "))
print("BCNN cua 2 so a va b: ",a*b//gcd(a,b))
