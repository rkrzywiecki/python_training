class Dog:
    __counter: int = 0

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age
        Dog.__counter += 1

    def __str__(self):
        return self.__name + " " + str(self.age)


my_pet = Dog("Teddy", 1)
skates_pet = Dog("Foxy", 5)
adams_pet = Dog("Luna", 1)

print(my_pet._Dog__counter)
print(skates_pet._Dog__counter)
print(adams_pet._Dog__counter)

print(my_pet.__dict__)
print(Dog.__dict__)

if hasattr(my_pet, "name"):
    print("My pet is called", my_pet.name)
else:
    print("My pet has no name")

print(Dog.__name__)
print(type(my_pet).__name__)
print(my_pet)
print(skates_pet)
print(adams_pet)
