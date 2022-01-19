# Tạo lóp Diem với 2 thuộc tính hoành độ x, tung độ y
# Nạp chồng toán tử '+' để cộng 2 điểm
# Cho 3 điểm A,B,C. Tính toạ độ tổng A+B, A+C, B+C

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Diem(x, y)

A = Diem(10,20)
B = Diem(15,25)
C = Diem(20,30)
print("A: ", A.x, A.y)
print("B: ", B.x, B.y)
print("C: ", C.x, C.y)
print("{} + {} = {} ".format(A, B, A + B))
print("{} + {} = {} ".format(A, C, A + C))
print("{} + {} = {} ".format(B, C, B + C))