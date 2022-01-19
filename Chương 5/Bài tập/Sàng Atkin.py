# Tất cả các số dư là số dư khi chia cho 60(chia cho 60 và xét số dư)
# Tất cả các số, bao gồm cả x và y đều là số dương
# Đảo 1 ô trong sàng nghĩa là thay dổi đánh dấu(là số nguyên tố hoặc không) thành ngược lại
# 1. Tạo bảng kết quả, điền vào 2, 3 và 5
# 2. Tạo bảo sàng nguyên tố với các số nguyên dương; tất cả các số đánh dấu đều không nguyên tố
# 3. Với tất cả các số trong sàng
# 4. Bất đầu từ số nhỏ nhất trong sàng
# 5. Lấy các số tiếp theo trong sàng được đánh dấu là nguyên tố
# 6. Thêm vào danh sách kết quả
# 7. Bình phương số đó và đánh dấu các bội số của số đó là không phải số nguyên tố
# 8. Lặp lại bước 5 cho tới bước 8

from math import *
def Sieve_Of_Atkin(N):
    sieve = []
    for i in range(N + 1):          #Tăng thêm 1
        sieve.append(False)
    if N > 2:
        sieve[2] = True
    if N > 3:
        sieve[2] = sieve[3]= True
    can2 = int(sqrt(N)) + 1
    for x in range(1, can2):
        for y in range(1, can2):
            n = (4 * x * x) + (y * y) 
            if(n <= N and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] = True
            
            n = (3 * x * x) + (y * y)
            if(n <= N and n % 12 == 7):
                sieve[n] = True
            
            n = (3 * x * x) - (y * y)
            if(x > y and n <= N and n % 12 == 11):
                sieve[n]= True
    r = 5
    while r*r < N:
        if sieve[r]:
            for i in range(r*r, N, r):
                sieve[i] = False
        r += 1
    for i in range(0, N + 1):
        if sieve[i]:
            print(i, end = " ")
n = -1
while n < 100:
    n = int(input('N = '))
Sieve_Of_Atkin(n)
