from animals import Animal
from exceptions import MaximumAdoptionReachedError
import re

class Adopter:

    def __init__(self, name:str, phone:str, national_id:str)->None:
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number.")
        if not self.validate_national_id(national_id):
            raise ValueError("Invalid national ID.")
        self.name = name
        self.phone = phone
        self.national_id = national_id
        self.adopted_animals = []


    @staticmethod
    def validate_phone(phone: str)->bool:
        """Validates an Iranian phone number."""
        pattern = r"^09\d{9}$"
        return bool(re.match(pattern, phone))


    @staticmethod
    def validate_national_id(national_id: str)->bool:
        """Validates an Iranian national ID."""
        pattern = r"^\d{10}$"
        return bool(re.match(pattern, national_id))

    def adopt_animal(self, animal:Animal)->None:
        """Adds an animal to the adopter's adopted list."""
        # Check if the adopter has reached the maximum limit
        if len(self.adopted_animals) >= 9:
            raise MaximumAdoptionReachedError(f"{self.name} has reached the maximum adoption limit.")
        # Add the animal to the list
        self.adopted_animals.append(animal)
        print(f"{animal.name} has been added to {self.name}'s adopted animals.")
        