a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a + b > c and b + c > a and a + c > b:
    print("a, b, c la 3 canh cua mot tam giac. ")

else:
    print("a, b, c khong la 3 canh cua mot tam giac. ")

if a == b == c:
    print("a, b, c la tam giac deu")

elif a == b != c:
    print("a, b, c la tam giac can")

else:
    print("a, b, c la tam giac thuong")