# Tạo Tuple P gồm các số nguyên tố nhỏ hơn 1 triệu.
# Số nguyên tố là số tự nhiên có 2 ước sô là 1 và chính nó

N = 10**7
L = [1 for i in range(N)]
L[0] = L[1] = 0
can2 = int(N**(1/2))
for i in range(2, 1 + can2):
    if L[i] == 1:
        k = i
        while i*k < N:
            k = k + 1
NT = tuple(i for i in range(N) if L[i] == 1 )        #NT:list nguyên tố
print("Danh sách các số nguyên tố nhỏ hơn %d: "%N)
print(NT)