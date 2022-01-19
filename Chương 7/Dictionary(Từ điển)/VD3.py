# Tra cứu điểm thi

n = int(input("Nhập số thí sinh n = "))
D = {}
print("Nhập SBD, họ tên và điểm của n thí sinh: ")
for i in range(n):
    SBD = input("SBD: ")
    ten = input("Tên: ")
    diem = int(input("Điểm: "))
    D[SBD] = [ten,diem]
print("Tra cứu: ")
SBD = input("Nhập SBD cần tra cứu: ")
print(D.get(SBD, "Không có thí sinh này!"))