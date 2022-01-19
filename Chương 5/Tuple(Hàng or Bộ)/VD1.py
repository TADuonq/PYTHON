#Viết chương trình nhập vào 1 bộ(tuple) gồm n số nguyên
#Tính tổng các số nguyên lẻ/chẵn trong tuple

n = -1              #Thiết kế điều kiện lặp
while(n < 0):
    n = int(input("Nhập n = "))
print("Nhập", n, "phần tử cho Tuple: ")
P = ()              #Khởi tạo Tuple
for i in range(n):
    x = int(input())
    P += (x,)

print("Tuple vừa nhập, P = ", P)
chan = le = 0 
for x in P:
    if x % 2 == 0:
        chan += x
    else:
        le += x

print("Tổng số chẵn trong Tuple P: ", chan)
print("Tổng số lẻ trong Tuple P: ", le)

