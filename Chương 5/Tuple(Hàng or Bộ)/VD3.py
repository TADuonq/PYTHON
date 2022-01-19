#Tạo Tuple P gồm các số nguyên tố nhỏ hơn n.
#Số nguyên tố là số tự nhiên có 2 ước số là 1 và chính nó

def nguyento(n):
    if(n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = -1          #Thiết kế điều kiện lặp
while(n < 0):
    n = int(input("Nhập n = "))
P = ()          #Khởi tạo P
for i in range(n):
    if nguyento(i):
        P = P + (i,)
print("P = ", P)
print("In Tuple P gồm các số nguyên tố nhỏ hơn %d: " %n)
for x in P:
    print(x, end = " ")
