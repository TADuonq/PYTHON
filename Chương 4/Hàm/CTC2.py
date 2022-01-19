#Chương trình con

def Tong_chan_le(*a):
    def Tong_chan():
        s = 0
        for x in a:
            if x % 2 == 0:
                s = s + x
        return s
    def Tong_le():
        s = 0
        for x in a:
            if x % 2 != 0:
                s = s + x 
        return s
    print('Tổng chẵn: ', Tong_chan())
    print('Tổng lẻ: ', Tong_le())
Tong_chan_le(1,2,3,4,5,6)