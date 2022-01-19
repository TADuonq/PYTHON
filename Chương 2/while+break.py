# Kiểm tra xem 1 số dương N có thuộc dãy số Fibonacci hay không?
n = int(input("Nhập số dương N: "))
a, b = 0, 1                 # Kiểu gán trong python: a = 0, b = 1
while b != n:
    if b>n:                 # Nếu b vượt quá n thì dừng
        break
    a, b = b, a + b         # a = b, b = a + b
print('Fibonacci' if b == n else 'Non-Fibonacci')