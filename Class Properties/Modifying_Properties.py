class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name


p1 = Person("Kitikon")
p2 = Person("June")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)
