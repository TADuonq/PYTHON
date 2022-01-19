# Chương trình con

def Tong_chan_le(a):
    def Tong_chan():
        s = 0
        for x in range(a):
            if x % 2 == 0:
                s = s + x
        return s
    def Tong_le():
        s = 0
        for x in range(a):
            if x % 2 != 0:
                s = s + x
        return s
    print('Tong chan: ', Tong_chan())
    print('Tong le: ', Tong_le())
Tong_chan_le(100)