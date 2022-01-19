# Xây dựng lớp 'vecter' có thuộc tính x và y, có phép toán cộng, trừ và tích vô hướng
# Cho 2 vecter u và v . Tính tổng, hiệu, tích vô hướng của 2 vecter

class vecto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

u = vecto(1, 2); print('u = ', u)
v = vecto(3, 4); print('v = ', v)
print("Tổng hai vecto: ", u + v)
print("Hiệu hai vecto: ", u - v)
print("Tích vô hướng: ", u * v)

