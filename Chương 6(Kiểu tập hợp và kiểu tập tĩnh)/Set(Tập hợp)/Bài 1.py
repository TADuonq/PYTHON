# Nhập 2 số tự nhiên a và b. Tính tổng các chữ số chung của 2 số

a = input("Nhập a = ")
b = input("Nhập b = ")
sum = 0
for i in range(10):
    if str(i) in a and str(i) in b:
        sum += i
print("Tổng các chữ số chung của a và b: ", sum)
