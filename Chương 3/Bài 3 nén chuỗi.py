s = input("Nhập xâu chữ cái cần nén: ")
st = ""
a = 1
n = len(s)
s = s + '0'
for i in range(n):
    if s[i] == s[i + 1]:
        a = a + 1
    elif a == 1:
        st = st + s[i]
    else:
        st = st + s[i] + str(a)
        a = 1
print("Chuỗi nén: ", st)