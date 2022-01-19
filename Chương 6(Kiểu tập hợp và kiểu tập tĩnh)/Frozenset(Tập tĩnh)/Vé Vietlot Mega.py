n = int(input("Nhập n = "))
A = ()
for i in range(1, 1 + n):
    so = (input("6 số Vietlot của người %d: "%i)).split()
    set1 = set()
    for x in so:
        set1.add(int(x))
    A = A + (set1,)

print("Nhập 6 số giải đặc biệt: ")
B = {int(input("số %d: "%i)) for i in range(1,7)}
print("In các bộ số thắng cuộc: ")
for x in A:
    if len(x & B) == 5:
        print(x)