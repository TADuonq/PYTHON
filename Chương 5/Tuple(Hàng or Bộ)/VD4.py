#Tuple P chứa các số nguyên tố trong khoảng n đến 2n

def nguyento(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = -1 
while (n < 0):
    n = int(input("Nhập n = "))
P = ()
for i in range(n, 2*n + 1):
    if nguyento(i):
        P = P + (i,)
print("In Tuple gồm các số nguyên tố từ n đến 2n: ", P)
for x in P:
    print(x, end = " ")