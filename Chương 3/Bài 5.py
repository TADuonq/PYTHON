# Chuỗi hoán vị
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
s1 = ''.join(sorted(s1))
s2 = ''.join(sorted(s2))
if s1 == s2:
    print("Hai chuỗi là hoán vị. ")
else:
    print("Hai chuỗi không là hoán vị. ")