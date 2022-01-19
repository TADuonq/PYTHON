#Kế thừa đa cấp khi 1 lớp dẫn xuất kế thừa 1 lớp dẫn khác
# Không có giới hạn về cấp độ, kế thừa đa cấp trong Python

class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("Gou gou!")
class DogChild(Dog):
    def eat(self):
        print("Eating milk ...")
d = DogChild()
d.bark()
d.speak()
d.eat()
d.speak()