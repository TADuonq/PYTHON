# Liệt kê các chuỗi ngoặc đúng độ dài ít hơn N của tuple X

def NgoacDung(i, T):
    for j in ['(',')']:
        if D[j] + 1 <= n//2:
            D[j] = D[j] + 1
            X[i] = j
            if D['('] >= D[')']:
                if(i == n - 1):
                    s = " "
                    for x in X:
                        s = s + x       #Đổi list về str
                    T.add(s)
                else:
                    NgoacDung(i + 1, T)
            D[j] = D[j] - 1

N = int(input("N = "))
T = set()
for n in range(2, N, 2):
    D = {'(':0, ')':0}
    X = [''for i in range(n)]
    NgoacDung(0, T)
T = tuple(T)
print("Tuple chuỗi ngoặc đúng: ", T)
print("Tổng số chuỗi: ", len(T))
