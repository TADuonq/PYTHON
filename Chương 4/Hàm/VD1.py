# Trả về kết quả từ hàm


def func1():
    return 1001                 # Trả về một loại kết quả
def func2():
    return('None')              # Không trả về kết quả
def func3():
    return 1001, 'abc', 4.5     # Trả về phức hợp nhiều loại
def func4(n):
    if n < 0:
        return 'số âm'          # Trả về chuỗi
    else:
        return n + 1            # Trả về số

print(func1())
print(func2())
print(func3())
print(func4(-12))
print(func4(2))