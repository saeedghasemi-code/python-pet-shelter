from animals import Animal, Dog, Cat, Bird, Snake
from shelter import Shelter
from people import Adopter
from exceptions import AnimalAlreadyAdoptedError, AnimalNotFoundError, DuplicateAnimalError, MaximumAdoptionReachedError


shelter = Shelter()

while True:
    print("1. Add Animal")
    print("2. Show Animals")
    print("3. Search Animal")
    print("4. Adopt Animal")
    print("5. Return Animal")
    print("6. Show Available Animals")
    print("7. Show Adopted Animals")
    print("8. Exit")


    choice = input("Enter choice: ")

    if choice == "1":
        animal_type = input("Enter animal type: ")
        name = input("Enter animal name: ")

        try:
            age = int(input("Enter animal age: "))
        except ValueError:
            print("Invalid age.")
            continue
        gender = input("Enter animal gender: ")
        breed = input("Enter animal breed: ")

        if animal_type == "Dog":
            animal = Dog(name, age, gender, breed)
        elif animal_type == "Cat":
            animal = Cat(name, age, gender, breed)
        elif animal_type == "Bird":
            animal = Bird(name, age, gender, breed)
        elif animal_type == "Snake":
            animal = Snake(name, age, gender, breed)
        else:
            print("Invalid animal type.")
            continue
        try:
            shelter.add_animal(animal)
        except DuplicateAnimalError as e:
            print(f"Error: {e}")


    elif choice == "2":
        shelter.show_animals()

    elif choice == "3":
        name = input("Enter animal name: ")
        animal = shelter.search_animal(name)
        if animal:
            print(animal.show_info())


    elif choice == "4":
        name = input("Enter animal name: ")
        adopter_name = input("Enter your name: ")
        adopter_phone = input("Enter your phone: ")
        adopter_national_id = input("Enter your national ID: ")
        try:
            adopter = Adopter(adopter_name, adopter_phone, adopter_national_id)
            shelter.adopt_animal(name, adopter)
        except ValueError as e:
            print(f"Error: {e}")
        except AnimalAlreadyAdoptedError as e:
            print(f"Error: {e}")
        except AnimalNotFoundError as e:
            print(f"Error: {e}")
        except MaximumAdoptionReachedError as e:
            print(f"Error: {e}")



    elif choice == "5":
        name = input("Enter animal name: ")
        try:
            shelter.return_animal(name)
        except AnimalNotFoundError as e:
            print(f"Error: {e}")


    elif choice == "6":
        shelter.show_available_animals()


    elif  choice == "7":
        shelter.show_adopted_animals()

    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")






