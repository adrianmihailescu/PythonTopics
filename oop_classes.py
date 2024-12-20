class Dog:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Rex", 5)
my_dog.bark()
