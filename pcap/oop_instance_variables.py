class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age


dog_1 = Dog("Teddy", 2)
print(dog_1.__dict__)
print(dog_1._Dog__name)