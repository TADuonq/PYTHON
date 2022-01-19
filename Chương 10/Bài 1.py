#Xây dựng lớp Rectange lưu thông tin về HCN có thuộc tính: chiều dài, chiều rộng và các phương thức tính chu vi và diện tích HCN



class Rectange:
       def __init__(self, dai, rong):
              self.dai = dai
              self.rong = rong
       def Chuvi(self):
              return 2*(self.dai + self.rong)
       def Dientich(self):
              return self.dai * self.rong
class RectangeSort(Rectange):
       def __init__(self, dai, rong):
              super().__init__(dai,rong)
       def __lt__(self,other):
              dt_self = self.Dientich()
              dt_other = other.Dientich()
              cv_self = self.Chuvi()
              cv_other = other.Chuvi()
              if dt_self < dt_other:
                     return True
              if dt_self == dt_other and cv_self < cv_other:
                     return True
              return False

n = int(input("n = "))
print("Nhập thông của n HCN: ")
L = []
for i in range(n):
       dai = float(input("Dai: "))
       rong = float(input("Rong: "))
       L.append(RectangeSort(dai,rong))
L.sort()
print("Danh sách HCN đã sắp xếp: ")
print("Dài\tRộng\tDiện tích\tChu vi")
for x in L:
       print(x.dai, "\t", x.rong, "\t", x.Dientich(), "\t\t", x.Chuvi())