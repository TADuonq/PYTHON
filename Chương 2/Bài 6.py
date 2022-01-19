# Cho 2 số tự nhiên a và b (1 <= a,b <= 10000). Tìm tất cả các số hoàn hảo trong[a,b]

a = int(input("Nhap so tu nhien a = "))
while a < 1 or a > 10000:
    a = int(input("Nhap so tu nhien a = "))
b = int(input("Nhap so tu nhien b = "))
while b < 1 or b > 10000:
    b = int(input("Nhap so tu nhien b = "))
if a > b:
    a, b = b, a
dem = 0
print("Cac so hoan hao trong doan [a,b] ")
for n in range(a, b + 1):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s = s + i
    if s == 2*n:
        dem += 1
        print(n)
if dem:
    print("Co", dem, "so hoan hao! ")
else:
    print("Khong co so hoan hao! ")