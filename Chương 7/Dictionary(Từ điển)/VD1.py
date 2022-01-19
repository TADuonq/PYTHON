#Tạo từ điển

n = int(input("Nhập n = "))
print("Nhập DS n số khác nhau: ")
L1 = [int(input()) for i in range(n)]
print("Nhập DS n tên: ")
L2 = [input()for i in range(n)]
D = {}
for i in range(n):
    D[L1[i]] = L2[i]
print("Nội dung từ điển: ")
for x,y in D.items():
    print(x, ": ", y)