class Vet:
    __animal = []

    def __init__(self, name):
        self.name = name
        self.animal = []
        self.space = 5

    def register_animal(self, animal_name):
        counter = 0
        if counter < self.space:
            self.animal.append(animal_name)
            self.__animal.append(animal_name)
            counter += 1
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name in self.animal:
            self.animal.remove(animal_name)
            self.animal.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animal)} animals. {self.space- (len(self.animal))} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
