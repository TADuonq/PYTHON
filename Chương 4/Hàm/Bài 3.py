#Nhập vào 1 số nguyên n. Viết chương trình ktra xem số nguyên n nhập vào có là số đối xứng hay không

import re


def doixung(n):
    temp = n
    s = 0
    while temp != 0:
        r = temp % 10
        s = s * 10 + r
        temp //= 10
    if s == n:
        return True
    else:
        return False

n = int(input("Nhập số nguyên n = "))
if(doixung(n)):
    print("Só", n, "là đối xứng!")
else:
    print("Số", n, "không đối xứng!")