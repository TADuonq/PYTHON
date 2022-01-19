#In ra các số tự nhiên chia hết cho 7 nhỏ hơn 100
n = 0
while n < 100:
    if(n % 7) == 0:
        print(n)
    n += 1

#Tính tổng các số nhỏ hơn 100 và không chia hết cho 5
t = 0
n = 0
while n < 1000:
    if (n % 5) != 0:
        t = t + n
    n += 1
print(t)