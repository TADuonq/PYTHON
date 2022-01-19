for x in range(1, 10):
    if(x == 5):
        break
    print("x = ", x)

for x in range(1, 5):
    for y in range(1, 3):
        if y == 2:
            break
    print("x = ", x, "y = ", y, sep = " ")