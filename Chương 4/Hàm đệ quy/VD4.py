# Viết chương trình tìm số Fibonacci thứ n sử dụng đệ quy
#       F(0) = 0, F(1) = 1, 
#       F(n) = F(n -2) + F(n -1) với mọi m >= 2



def Fibonacci(n):
    if n < 0: 
        return "n không hợp lệ"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input("Cho n = "))
print("Số Fibonacci thứ", n, "là: ", Fibonacci(n))
print("Dãy số Fibonacci:")
for i in range(n + 1):
    print(Fibonacci(i), end = " ")