#Hãy tạp lớp TamGiac kế thừa từ lớp DaGiac
# Bổ sung thêm phương thức tính diện tích tam giác

class DaGiac:
    def __init__(self, socanh):
        self.n = socanh
        self.canh = [0 for i in range(socanh)]
    def nhapcanh(self):
        self.canh = [float(input("Nhập cạnh " + str(i + 1)+ ": ")) for i in range(self.n)]
    def hienthicanh(self):
        for i in range(self.n):
            print("Giá trị cạnh", i+1, "là: ", self.canh[i])
class TamGiac(DaGiac):
    def __init__(self):
        DaGiac.__init__(self, 3)
    def dientich(self):
        a, b, c = self.canh
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print('Diện tích tam giác: %.2f' %area)
t = TamGiac()
t.nhapcanh()
t.hienthicanh()
t.dientich()