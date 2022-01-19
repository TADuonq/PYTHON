a = float(input("He so a = "))
b = float(input("He so b = "))
c = float(input("He so c = "))
delta = b*b - 4*a*c
if delta<0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    x = -b/(2*a)
    print("Phuong trin co mot nghiem kep: x = ", x)
else:
    from math import sqrt
    x1 = (-b + sqrt(delta))/(2*a)
    x2 = (-b - sqrt(delta))/(2*a)
    print("Phuong trinh co hai nghiem phan biet:")
    print("x1 = ", x1)
    print("x2 = ", x2)
