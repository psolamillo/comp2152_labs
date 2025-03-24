from Person import Person


class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        print("This time it's a student object")
        self.major = major

s1 = Student("Maria",22,6,"Computer Science")
print(s1.name)
