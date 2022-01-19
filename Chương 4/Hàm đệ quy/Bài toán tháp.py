def TowerHN(n, a, b, c):
    if n == 1:
        print(a, "--->", c)
    else:
        TowerHN(n-1, a, c, b)
        TowerHN(1, a, b, c)
        TowerHN(n-1, b, a, c)

a = 'A'
b = 'B'
c = 'C'
n = int(input("Nhập số tầng n = "))
print("Trình tự chuyển các đĩa: ")
TowerHN(n, a, b, c)