# Thống kê điểm thi
# Viết chương trình nhập thông tin của SV gồm: Điểm, họ tên và lưu vào 1 từ điển
# Điểm thuộc {0,1, 2,..,10}, sau đó thống kê những bạn được điểm 10, 9,...,0

n = int(input("Nhập số SV n = "))
D = {}
for i in range(11):
    D[i] = []
print("Nhập tên và điểm của n SV: ")
for i in range(n):
    ten = input("Tên: ")
    diem = int(input("Điểm: "))
    D[diem].append(ten)
print("Thống kê: ")
for i in D:
    print("SV được điểm", i, ": ")
    print(D[i])