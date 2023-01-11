# classes in python
# class used to model in real world object
class Point:
    # constructors is a function that crated when the object is created
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('Move')

    def draw(self):
        print('Draw')


# object is an instance of class
# objects are example of class
point1 = Point(67, 45)
print(point1.x)
point1.draw()
point1.a = 34
point1.b = 45
print(point1.a)
point1.move()
# exercise


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} says \"I am very happy with python\"')


person = Person("Haile")
person.talk()
