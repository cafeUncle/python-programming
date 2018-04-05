class Animal:
    __name = ""
    __height = ""
    __weight = ""
    __sound = ""

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
        print('父类构造')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        return "Animal"

    def to_string(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name, self.__height, self.__weight, self.__sound)

cat = Animal('cat', 30, 3, 'miaomiao')

print(cat.to_string())
print(cat.get_type())


class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        super().__init__(name, height, weight, sound)  # python的父类构造需要显式调用
        self.__owner = owner
        print('子类构造')
        # super(Dog, self).__init__(name, height, weight, sound)

    def get_type(self):
        print('先手动调用一下父类的get_type试试能不能:', super().get_type())
        return "Dog"

    def to_string(self):
        return "{} is {} cm tall and {} kilograms and say {} and its owner is {}"\
            .format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog('spot', 53, 27, "Ruff", "Derek")
print(spot.to_string())
spot.multiple_sounds(3)
print(spot.get_type())


class AnimalTesting:
    def get_type(self, animal):
        if isinstance(animal, Animal):
            print(animal.get_type())
        else:
            print('类型不对')

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)
test_animals.get_type([1, 2, 3])
