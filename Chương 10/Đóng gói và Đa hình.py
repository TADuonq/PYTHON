class Lamboghini:
    def dungxe(self):
        print("Lamboghini dừng xe để đón người yêu")
    def nomay(self):
        print("Lamboghini nổ máy để đưa người yêu đi chơi")
    
class Ferrari:
    def dungxe(self):
        print("Ferrari dừng xe để đón bồ")
    def nomay(self):
        print("Ferrari nổ máy để đưa bồ đi nhà nghỉ")

def kiemtra_dungxe(car):
    car.dungxe()

Lamboghini = Lamboghini()
Ferrari = Ferrari()
kiemtra_dungxe(Lamboghini)
kiemtra_dungxe(Ferrari)