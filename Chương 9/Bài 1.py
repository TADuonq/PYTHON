filename = input("Ten file: ")
f = open(filename, 'w')
i = 0
while 1 > 0:
    i += 1
    s = input("Dong %d: "%i)
    if s != '':
        f.writelines(s + '\n')
    else:
        break
f.close()