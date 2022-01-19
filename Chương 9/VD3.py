f = open("vidu3.txt", 'w')
d = 0
for i in range(10,100):
    f.write(str(i) + ' ')
    d += 1
    if d % 10 == 0:
        f.write('\n')
f.close()