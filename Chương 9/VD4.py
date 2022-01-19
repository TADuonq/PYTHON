ten_file = input("Tên file: ")
f = open(ten_file, 'w')
d = 0
while 1 > 0:
    try:
        a = int("Nhập số nguyên dương: ")
        if a != '':
            if a.isdigit():
                f.write(a + ' ')
                d += 1
            else:
                raise ValueError("Không phải số nguyên dương. Nhập lại!")
            if d % 5 == 0:
                f.write('\n')
        else:
            break
    except ValueError as e:
        print(e)
        continue
f.close()    