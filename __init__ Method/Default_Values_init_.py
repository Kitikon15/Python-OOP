class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age


p1 = Person("Kitikon")
p2 = Person("June", 21)

print(p1.name, p1.age)
print(p2.name, p2.age)
