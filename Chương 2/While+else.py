# Nhập số n và kiểm tra xem nó có phải số nguyên tố hay không
# Chú ý: nếu không sử dụng else, ta sẽ phải khai báo thêm
# Biến phụ và chương trình dài hơn vài dòng

n = int(input("Nhập số N: "))
if n < 2:
    print("N không phải số nguyên tố")
else:
    x = 2
    while x < n:
        if (n % x) == 0:
            print(" không phải là số nguyên tố")
            break;
        x = x + 1
    else:
        print("N là số nguyên tố")