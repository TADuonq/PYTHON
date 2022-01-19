# Nhập vào 1 số nguyên n. In ra tất cả các số nguyên trong khoảng từ 1 đến n

#Cách 1
def nguyen_to(m):
    if(m <= 1):
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True
n = int(input("Nhập số nguyên dương n = "))
print("Các số nguyên tố trong khoảng từ 1 đến n: ")
for i in range(1, n+1):
    if nguyen_to(i):
        print(i, end = " ")

#Cách 2
def nguyen_to(m):
    if(m <= 1):
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n = "))
d = 0
print("Các số nguyên tố trong khảng từ 1 đến n: ")
for i in range(1, n + 1):
    if nguyen_to(i):
        d += 1
        if d == 1:
            print(i, end = " ")
        else:
            print(",", i, end = " ")
