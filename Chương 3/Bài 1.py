# Tách kí tự số và kí tự chữ cái

s = input("Nhập chuối gồm kí tự số và chữ cái La tinh: ")
s1 = s2 = ""
for u in s:
    if '0' <= u <= '9':
        s1 = s1 + u
    else:
        s2 = s2 + u
print("Xâu gồm các chữ số: ", s1)
print("Xâu gồm các chữ cái: ", s2)
