class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"


p1 = Person("Kitikon", 21)
print(p1.get_info())
