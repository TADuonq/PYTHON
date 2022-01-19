# Nhập danh sách các học sinh thi môn Toán, Lý, Hoá
# -HS chỉ thi môn Toán
# -HS chỉ thi môn Lý
# -HS thi môn Toán và Lý
# -HS thi môn Lý và Hoá
# - HS thi cả 3 môn 

a = int(input("Nhập số học sinh thi Toán: "))
print("Nhập", a, "học sinh thi Toán: ")
A = {input() for i in range(a)}

b = int(input("Nhập số học sinh thi Lý: "))
print("Nhập", b, "học sinh thi Lý: ")
B = {input() for i in range(b)}

c = int(input("Nhập số học sinh thi Hoá: "))
print("Nhập", c, "học sinh thi Hoá: ")
C = {input() for i in range(c)}

print("HS chỉ thi môn Toán: ", A - (B|C))
print("HS chỉ thi môn Lý: ", B - (A|C))
TLH = A & B & C
print("HS thi môn Toán và Lý: ", A & B - TLH)
print("HS thi môn Lý và Hoá: ", B & C - TLH)
print("HS thi cả ba môn: ", TLH)