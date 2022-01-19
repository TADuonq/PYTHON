#Câu lệnh continue được viết trong khối lện của các vòng lặp.
#Khi thực hiện câu lệnh continue, các câu lện phía sau sẽ không được thực hiện mà quay sang lần lượt lặp tiếp theo

for x in range(1, 10):
    if(x%2 == 0):
        continue
    print("x = ", x, "La so le. ")