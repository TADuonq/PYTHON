import math
tien = 1e7              # Số tiền đầu(10M)
lai = 5.1 / 100         # Lãi suất 5.1%
print("Số tiền có sau 10 năm: ", int(tien * (1 + lai)**10))
dich = 5e7              #Số tiền đích(50M)
nam = math.log(dich/tien,1+lai)     #tính theo log
print("Số năm để có ít nhất 50 triệu: ", math.ceil(nam))


