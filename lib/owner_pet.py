
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """
        Return all pets owned by this owner.
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Add an owner to a Pet instance.
        """
        if not isinstance(pet, Pet):
            raise Exception("Must add a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """
        Return pets sorted by their name.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance or None")
        self.owner = owner

        # keep track of all pets
        Pet.all.append(self)
