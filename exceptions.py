
class AnimalNotFoundError(Exception):
    """Raised when an animal is not found in the shelter."""
    pass

class DuplicateAnimalError(Exception):
    """Raised when trying to add an animal that already exists."""
    pass

class AnimalAlreadyAdoptedError(Exception):
    """Raised when trying to adopt an animal that is already adopted."""
    pass

class MaximumAdoptionReachedError(Exception):
    """Raised when an adopter has reached the maximum adoption limit."""
    pass