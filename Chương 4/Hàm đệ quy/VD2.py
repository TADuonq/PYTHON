#Tính tổ hợp chập k của n theo công thức hồi quy C(k,n)=C(k-1,n-1) + C(k,n-1)

def C(k,n):
    if k == n or k == 0:
        return 1
    else:
        return C(k-1,n-1) + C(k,n-1)

n = k = -1      #Thiết lập để nhập n và k
while(not(0 <= k <= n)):
    n = int(input("Cho n = "))
    k = int(input("Cho k = "))
    if not(0 <= k <= n):
        print("Nhập sai! Yêu cầu nhập lại n và k")

print("Tổ hợp C(k,n) = ", C(k,n))
