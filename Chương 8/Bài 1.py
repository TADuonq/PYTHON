# Viết chương trình nhập 2 số nguyên a và b, sau đó tính và in ra giá trị phân số a/b
# Chú ý xử lý ngoại lệ trong các tình hướng dưới đây:
#       + Người dùng nhập a hoặc b không phải số nguyên
#       + Người dùng nhập b = 0



while 1 > 0:
    try:
        a = int(input("Nhập só nguyên a: "))
        b = int(input("Nhập số nguyên b: "))
        u = a/b
    except ZeroDivisionError:
        print("Giá trị b = 0")
        print("Hãy nhập lại: ")
    except ValueError:
        print("Giá trị nhập vào không phải số nguyên! ")
        print("Hãy nhập lại: ")
    else:
        break

print("a/b = ", u)