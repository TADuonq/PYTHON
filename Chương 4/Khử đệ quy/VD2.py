# In n số Fibonacci không đệ quy

def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f1 = 0
        f2 = 1
        for k in range(2, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

n = int(input("Cho n = "))
print("Dãy số Fibonacci: " )
for i in range(n + 1):
    print(Fibo(i), end = " ")
