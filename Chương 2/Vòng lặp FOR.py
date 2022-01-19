n = int(input("Nhập giá trị n: "))
gt = 1 
for i in range(2, n+1):
    gt = gt * i
print("n! = ",gt)





def giaithua(n):
    gt = 1
    for i in range(2, n+1):
        gt = gt * i
    return gt 

n = int(input("Nhập giá trị n: "))
print("n! = ", giaithua(n))