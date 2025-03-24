class Person:

    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
        self.public_prop = "I'm public"
        print("Constructing the Person object")

    #Magic getter/setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")









#p1 = Person("Mark",20,6)
#print(p1.get_name())
#print(Person.get_name(p1))
#print(p1.name)
#print(p1.public_prop)

#p1.name("Anna")
#print(p1.name)



