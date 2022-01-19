f2 = open("vidu2.txt", 'w')
for i in range(5):
    for j in range(5):
        f2.write(str(i + j) + ' ')
    f2.write('\n')
f2.close()