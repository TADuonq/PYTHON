class Employee:
    __count = 0;
    def __init__(self):
        Employee.__count = Employee.__count + 1
    def display(self):
        print("số lượng nhân viên: ", Employee.__count)

emp1 = Employee()
try:
    print(emp1.__count)
except Exception as e:
    print(type(e), e)
finally:
    emp1.display()