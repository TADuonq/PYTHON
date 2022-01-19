# Nhập vào 1 số nguyên n. Kiểm tra n có phải là số nguyên tố

# Cách 1
def nguyen_to(n):
    if(n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n = "))
if nguyen_to(n):
    print("n la nguyên tố!")
else:
    print("n không là nguyên tố !")

# Cách 2
def nguyen_to1(n):
    if (n <= 1):
        return print("n không là nguyên tố !")
    for i in range(2, n):
        if n % i == 0:
            return print("n không là số nguyên tố !")
    return print("n là nguyên tố !")
n = int(input("Nhâọ n = "))
nguyen_to1(n)