class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def infor(self):
        print("Tên: ", self.ten)
        print("Tuổi: ", self.tuoi)

class Sinhvien(Nguoi):
    def __init__(self, ten, tuoi, nam):
        Nguoi.__init__(self, ten, tuoi)
        self.totnghiep = nam
    def infor(self):
        Nguoi.infor(self)
        print("Năm tốt nghiệp: ", self.totnghiep)

p = Sinhvien("Võ Thị Bích Ngọc", 19, 2024 )
p.infor()
p.ten = "Võ Thị Bích Ngọc(Cáo)"
p.totnghiep = 2025
print("Thông tin sau khi cập nhật:")
p.infor()