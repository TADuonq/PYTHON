a = int(input("a = "))
b = int(input("b = "))
if a<0 or b<0:
    a,b = abs(a),abs(b)
while(b>0):
    if(a>b):
        a, b = b, a % b
    else:
        a, b = a, b % a
print("UCLN = ", a)