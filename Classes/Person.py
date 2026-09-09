class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"Hlw {self.name} you are {self.age} year's old.")

person1 = person('Aman','20')
person1.get_info()
person2 = person('Faiz','49')
person2.get_info()