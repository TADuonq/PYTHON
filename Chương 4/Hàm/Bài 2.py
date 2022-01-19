#Nhập vào 1 số nguyên dương n. Viết chương trình phân tích n tích các thừa số nguyên tố

def nguyen_to(n):
    if(n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def thua_so_ngto(n):
    for i in range(2, n+1):
        while n%i == 0 and nguyen_to(i) == True:
            print(i, end = " ")
            n //= i
        
n = int(input("Nhập n = "))
print("Phân tích n ra các thừa số nguyên tố: ")
thua_so_ngto(n)