class Mammal:
    def __init__(self, mammalName):
        self.name = mammalName

    def walk(self):
        print(f'{self.name} can Walk.')


class Dog(Mammal):
    def __init__(self, mammalName):
        super().__init__(mammalName)

    def bark(self):
        print(f'{self.name} can Bark')


class Cat(Mammal):
    def __init__(self, mammalName):
        super().__init__(mammalName)

    def annoying(self):
        print(f'{self.name} Annoying')


dog = Dog('Dog')
cat = Cat('Cat')
dog.walk()
dog.bark()
cat.walk()
cat.annoying()
