f1 = open("dssv.txt", 'r')
f2 = open("phach.txt", 'r')
f3 = open("diem.txt", 'r')
dssv_line = f1.readlines()
phach_line = f2.readlines()
diem_line = f3.readlines()
dssv = {}
for x in dssv_line:
    x.strip()
    L = x.split(' ', 1)
    sbd = L[0].strip()
    hoten = L[1].strip()
    dssv[sbd] = hoten
print("\nSSSV: ", dssv)
phach = {}
for x in phach_line:
    x.strip()
    L = x.split()
    sbd = L[0].strip()
    ph = L[1].strip()
    phach[sbd] = ph
print("\nSBD-Phach: ", phach)
diem = {}
for x in diem_line:
    x.strip()
    L = x.split()
    ph = L[0].strip()
    di = L[1].strip()
    diem[ph] = di
print("\nPhach-Diem: ", diem)
KQ = []
for x,y in phach.items():
    SBD = x
    Diem = int(diem[y])
    Ten = dssv[SBD]
    KQ.append((SBD, Ten, Diem))
KQ.sort(key = lambda hs : hs[2], reverse = True)
print("Danh sách điểm sinh theo tứ tự giảm dần: ")
for x in KQ:
    print("{:5} {:<20} {:<5}".format(x[0], x[1], x[2]))
f4 = open("ketqua.txt", 'w')
for x in KQ:
    line = x[0] + ' ' + x[1] + ' ' + str(x[2])
    f4.write(line)
    f4.write('\n')
f1.close()
f2.close()
f3.close()
f4.close()