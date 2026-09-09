class Animal:
    def sound(self):
        print("Some sound")
class dog(Animal):
    def sound(self):
        print("Bark!")

d = Animal()
d.sound() #they print the some sound
d2 = dog()
d2.sound() #they print the bark!