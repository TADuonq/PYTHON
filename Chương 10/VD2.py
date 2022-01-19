# Xây dựng lớp 'Nguoi' có thuộc tính họ tên và tuổi, có phép toán so sánh theo tuổi
# Sử dụng phép toán so sánh để sắp xếp 1 danh sách đối tượng theo tuổi

class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def infor(self):
        print("Tên: ", self.ten)
        print("Tuổi: ", self.tuoi)
    def __lt__(self, other):
        return self.tuoi < other.tuoi

p1 = Nguoi("Trương Anh Dương", 22)
p2 = Nguoi("Võ Thị Bich Ngọc", 19)
p3 = Nguoi("Lê Nhất Chi Mai", 17)
ds = [p1, p2, p3]
ds.sort()
for x in ds:
    x.infor()