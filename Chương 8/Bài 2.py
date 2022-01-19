# Viết chương trình yêu cầu người dùng nhập a, b và c là độ dài 3 cạnh của 1 tam giác
# Xử lý ngoại lệ trong các tình huống sau
#       + Người dùng nhập a, b hoặc c không phải kiểu số
#       + Người dùng nhập giá trị 0 hoặc số âm cho a, b hoặc c không ph
#       + Người dùng nhập a,b,c dương nhưng không thể là cạnh của 1 tam giác

while 1 > 0:
    try:
        a = float(input("Nhập cạnh a = "))
        b = float(input("Nhập cạnh b = "))
        c = float(input("Nhập cạnh c = "))
        if a <= 0 or b <= 0 or c <= 0:
            raise Exception("Phải nhập số dương! ")
        if not(a + b > c and a + c > b and b + c > a):
            raise Exception("3 số không thoả mãn 3 canh tam giác!")
    except ValueError:
        print("Lỗi kiểu")
    except Exception as e:
        print(e)
    else:
        print("3 cạnh tam giác!") 
        break
print("Kết thúc")   