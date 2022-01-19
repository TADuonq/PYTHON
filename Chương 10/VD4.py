class Tinh1:
    def Cong(self, a, b):
        return a + b;
class Tinh2:
    def Nhan(self, a, b):
        return a * b;
class LopChia(Tinh1, Tinh2):
    def Chia(self, a, b):
        return a / b;
print("'LopChia' là con của 'Tinh2': ", issubclass(LopChia,Tinh2))
print("'Tinh1' là con cua 'Tinh2': ", issubclass(Tinh1,Tinh2))
d = LopChia()
print("Đối tượng d thể hiện của lớp 'LopChia': ", isinstance(d,LopChia))
