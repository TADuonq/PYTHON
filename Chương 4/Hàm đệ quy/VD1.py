#Tính n! theo đệ quy 0! = 1, n! = n*(n-1)!

def giaithua(n):
    if 0 <= n <= 1:
        return 1
    else:
        return n*giaithua(n - 1) 

n = int(input("Nhập n = "))
if n < 0:
    print("Số n không hợp lệ! ")
else:
    print(n, "! = ", giaithua(n))
