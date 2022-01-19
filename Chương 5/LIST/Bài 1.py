# Tính tổng các số nguyên lẻ. Nhập số nguyên dương n và danh sách n gồm số nguyên. Tính tổng các số nguyên dương lẻ

n = int(input("Nhập n = "))
list = []
for i in range(n):
    x = int(input())
    list.append(x)
s = 0
for x in list:
    if x > 0 and x % 2 !=0:
        s += x
print("Tổng các số hàng lẻ: ", s)
