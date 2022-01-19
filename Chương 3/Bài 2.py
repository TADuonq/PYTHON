# Một chuỗi được gọi là chuỗi đối xứng nếu đọc chúng từ trái sang phải cũng giống như đọc từ phải sang trái
# Ví dụ: "madam", "1221" là các chuối đối xứng, chuỗi "12334" không phải là chuỗi đối xứng
# Viết chương trình nhập vào một chuỗi và ktra xem có phải chuỗi đối xứng không

# Minh hoạ 1
s = input("Nhập chuỗi S = ")
while(s != ""):
    n = len(s)
    dx = True
    for i in range(n):
        if s[i] != s[n - 1 - i]:
            dx = False
            break
    if dx == True:
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                dx = False
                break
        print("Chuỗi s đối xứng! ")
    else:
        print("Chuỗi s không đối xứng!")
    s = input("Kiểm tra tiếp? Nhập chuỗi s = ")


# Minh hoạ 2
s = input("Nhập chuỗi s = ")
while(s != ""):
    w = s[::-1]
    if w == s:
        print("Chuỗi s đối xứng")
    else:
        print("Chuỗi s không đối xứng")
    s = input("Kiểm tra tiếp? Nhập chuỗi s = S")