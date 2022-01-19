# Lưu thông tin của n sinh viên trong 1 danh sách L, mà mỗi phần tử của danh sách là 1 bộ(Tên, Điểm Toán, Điểm Tin, Điểm Anh)

n = int(input("Nhập n = "))
print("Nhập tên: ")
Ten = [input() for i in range(n)]
print("Nhập Điểm Toán: ")
Toan = [float(input()) for i in range(n)]
print("Nhập Điểm Tin: ")
Tin = [float(input()) for i in range(n)]
print("Nhập Điểm Anh: ")
Anh = [float(input()) for i in range(n)]
SV = list(zip(Ten, Toan, Tin, Anh))
T = []
for i in range(n):
    T.append((SV[i][0], SV[i][1], SV[i][2], SV[i][3]))
for i in range(n):
    print(T[i])