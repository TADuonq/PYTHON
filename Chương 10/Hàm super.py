class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def infor(self):
        print("Tên: ", self.ten)
        print("Tuổi: ", self.tuoi)
class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, nam):
        super().__init__(ten, tuoi)
        self.totngihep = nam
    def infor(self):
        super().infor()
        print("Năm tốt nghiệp: ", self.totngihep)

p = SinhVien("Võ Thị Bích Ngọc", 22, 2023)
p.infor()