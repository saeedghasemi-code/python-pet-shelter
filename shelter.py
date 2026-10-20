from animals import Animal
from exceptions import AnimalNotFoundError, DuplicateAnimalError, AnimalAlreadyAdoptedError
from decorators import log_action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from people import Adopter

class Shelter:
    def __init__(self)-> None:
        self.animals = []


    @log_action
    def add_animal(self, animal:Animal)->None:

        for a in self.animals:
            if a.name == animal.name:
                raise DuplicateAnimalError(f"Animal '{animal.name}' already exists.")
        self.animals.append(animal)
        print(f"{animal.name} has been added to the shelter.")



    def remove_animal(self, name:str)->None:
        """Removes an animal from the shelter by name."""
        for a in self.animals:
            if a.name == name:
                self.animals.remove(a)
                print(f"{name} has been removed from the shelter.")
                return
        raise AnimalNotFoundError(f"Animal '{name}' not found")


    def search_animal(self, name:str)->Animal | None:
        """Searches for an animal by name and returns it."""
        for a in self.animals:
            if a.name == name:
                return a    
        print("Not found.")
        return None



    def show_animals(self)->None:
        """Display all animals in the shelter"""
        # Check if the shelter is empty
        if not self.animals:
            print("No animals in the shelter.") 
            return
        # Display each animal
        for a in self.animals:
            print(f"{a.show_info()}")



    def adopt_animal(self, name:str, adopter)->None:
        """Adopts an animal by name."""
        animal = self.search_animal(name)
        if animal is None:
            raise AnimalNotFoundError(f"Animal '{name}' not found.")
        if animal.adopted == True:
            raise AnimalAlreadyAdoptedError(f"Animal '{name}' is already adopted.")
        adopter.adopt_animal(animal)
        animal.adopted = True
        print(f"{animal.name} has been adopted!")


    def return_animal(self, name:str)->None:
        """Returns an adopted animal back to the shelter."""
        animal = self.search_animal(name)
        if animal is None:
            raise AnimalNotFoundError(f"Animal '{name}' not found.")
        if animal.adopted == False:
            print("Animal not adopted")
            return
        animal.adopted = False
        print("Return successful.")


    def show_available_animals(self)-> None:
        """Display all available (not adopted) animals."""
        for a in self.animals:
            if a.adopted == False:
                print(a.show_info())


    def show_adopted_animals(self)->None:
        """Display all adopted animals"""
        for a in self.animals:
            if a.adopted == True:
                print(a.show_info())

