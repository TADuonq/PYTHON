# Nhập 3 số thực a, b, c. TÍnh TBC f(a), f(b), f(c) nếu biết f(x) = x**5 + x**2

def f(x):
    return x**5 + x**2
a = float(input("Nhập số thực a = "))
b = float(input("Nhập số thực b = "))
c = float(input("Nhập số thực c = "))

ftb = (f(a) + f(b) + f(c))/3
print('TBC của hàm f là: ',ftb)
print('TBC của hàm f: %f ' %ftb)
print('TBC của hàm f: %10.5f' %ftb)
