class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

person = Person("Alice", 30)
print(person.get_name())
print(person.get_age())
person.set_age(31)
print(person.get_age())