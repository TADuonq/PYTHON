# Giải phương trình x**3 - x - 1 = 0 trên đoạn [1,2]

def f(x): 
    return x**3 - x - 1
def chiadoi(a,b,e):
    c = (a + b) / 2
    if f(a) * f(b) and abs(b -a) < e:
        return c
    elif f(a) * f(c) < 0:
        return chiadoi(a,c,e)
    else:
        return chiadoi(b,c,e)
    

a = 1
b = 2
e = 0.0001
x = chiadoi(a,b,e)
print("Giải phương trình f(x) = 0")
print("Nghiệm x = %6.4f" %x)