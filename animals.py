class Animal:
    def __init__(self, name:str, age:int, gender:str, breed:str)->None:
        """Initializes a new Animal."""
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.adopted = False


    @property
    def status(self)->str:
        """Returns the adoption status of the animal."""
        return "Adopted" if self.adopted else "Available"


    @staticmethod
    def from_dict(data: dict)->"Animal":
        """Creates an Animal object from a dictionary."""
        return Animal(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            breed=data["breed"],
            )

    def show_info(self)->str:
        return f"Name: {self.name} | Age: {self.age} | Gender: {self.gender} | Breed: {self.breed} | Adopted: {self.adopted}"


    def make_sound(self)->str:
        """Returns the sound the animal makes."""
        return "Some generic animal sound"




class Dog(Animal):
    """Represents a dog in the shelter."""
    def make_sound(self)->str:
        """Returns the sound a dog makes."""
        return "Woof!"


class Cat(Animal):
    """Represents a cat in the shelter."""
    def make_sound(self)->str:
        """Returns the sound a cat makes."""
        return "Meow!"

class Bird(Animal):
    """Represents a bird in the shelter."""
    def make_sound(self)->str:
        """Returns the sound a bird makes."""
        return "Tweet!"

class Snake(Animal):
    """Represents a snake in the shelter."""
    def make_sound(self)->str:
        """Returns the sound a snake makes."""
        return "Hiss!"
