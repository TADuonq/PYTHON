# Tách từ trong chuỗi

s = input("Nhập chuỗi chuẩn: ")
list1 = s.split(' ')
list2 = []
for x in list1:
    list2 = list2 + x.split(',')
print("Các từ trong chuỗi: ")
for x in list2:
    if x != '':
        print(x)
st = input("Nhập chuỗi chuẩn: ")
list3 = st.split()
for x in list3:
    print(x)