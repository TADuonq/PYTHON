# Hàm tạo có tham số

class Car:
    loaixe = "Ô tô"
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

Lamboghini = Car("Lamboghini", "Trắng", "Xăng pha điện")
Ferrari = Car("Ferari", "Đỏ", "Xăng")
Audi = Car("Audi", "Xám", "Điện")

print("Audi là {}".format(Audi.loaixe))
print("Lamboghini là {}".format(Lamboghini.loaixe))
print("Ferrari là {}".format(Ferrari.loaixe))
print("Xe {} có màu {}, {} là nguyên liệu vận hành".format(Lamboghini.tenxe, Lamboghini.mausac, Lamboghini.nguyenlieu))
print("Xe {} có màu {}, {} là nguyên liệu vận hành".format(Ferrari.tenxe, Ferrari.mausac, Ferrari.nguyenlieu))
print("Xe {} có màu {}, {} là nguyên liệu vận hành".format(Audi.tenxe, Audi.mausac, Audi.nguyenlieu))