# Viết chương trình tính n! không sử dụng đệ quy n! = 1.2... n

def giaithua1(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

n = int(input("Nhập n = "))
if n < 0:
    print("Số n không hợp lệ! ")
else:
    print(n, "! = ", giaithua1(n))