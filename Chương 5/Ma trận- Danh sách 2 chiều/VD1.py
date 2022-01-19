#Viết chương trình nhập vào 1 ma trận gồm m hàng và n cột
# In ra ma trận được nhập

m = int(input("Nhập hàng m = "))
n = int(input("Nhập số cột n = "))
A = []              #Tạo ma trận rỗng
for i in range(m):
    row = []        #tạo dòng rỗng
    for j in range(n):
        x = int(input())
        row.append(x)
    A.append(row)   #Thêm dòng vào ma trận
for x in A:
    print(x)
